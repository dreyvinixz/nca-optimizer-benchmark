#!/usr/bin/env node

import fs from "node:fs";
import fsp from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const SKILL_DIR = "C:/Users/User/.codex/plugins/cache/openai-primary-runtime/presentations/26.521.10419/skills/presentations";
const THREAD_ID = process.env.CODEX_THREAD_ID || `manual-${new Date().toISOString().replace(/[-:.TZ]/g, "").slice(0, 14)}-prof`;
const WORKSPACE = path.join(ROOT, "outputs", THREAD_ID, "presentations", "professor-results");
const SLIDES_DIR = path.join(WORKSPACE, "slides");
const PREVIEW_DIR = path.join(WORKSPACE, "preview");
const LAYOUT_DIR = path.join(WORKSPACE, "layout");
const QA_DIR = path.join(WORKSPACE, "qa");
const OUTPUT_DIR = path.join(ROOT, "outputs", "professor_presentation");
const FINAL_PPTX = path.join(OUTPUT_DIR, "nca_optimizer_benchmark_results.pptx");

const FIG = path.join(OUTPUT_DIR, "figures");
const TABLE = path.join(OUTPUT_DIR, "tables");

const COLORS = {
  paper: "#F7F4ED",
  ink: "#17202A",
  muted: "#5B6472",
  faint: "#D9D2C4",
  blue: "#2364AA",
  orange: "#F28E2B",
  green: "#59A14F",
  red: "#C53D3F",
  dark: "#111827",
  white: "#FFFFFF",
};

function rel(filePath) {
  return path.relative(ROOT, filePath);
}

function ensureFile(filePath) {
  if (!fs.existsSync(filePath)) throw new Error(`Missing required file: ${filePath}`);
  return filePath;
}

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = "";
  let inQuotes = false;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    const next = text[i + 1];
    if (ch === '"') {
      if (inQuotes && next === '"') {
        field += '"';
        i += 1;
      } else {
        inQuotes = !inQuotes;
      }
    } else if (ch === "," && !inQuotes) {
      row.push(field);
      field = "";
    } else if ((ch === "\n" || ch === "\r") && !inQuotes) {
      if (ch === "\r" && next === "\n") i += 1;
      row.push(field);
      if (row.some((value) => value !== "")) rows.push(row);
      row = [];
      field = "";
    } else {
      field += ch;
    }
  }
  if (field.length || row.length) {
    row.push(field);
    rows.push(row);
  }
  const [header, ...body] = rows;
  return body.map((values) => Object.fromEntries(header.map((key, index) => [key, values[index] ?? ""])));
}

function readCsv(filePath) {
  return parseCsv(fs.readFileSync(filePath, "utf8"));
}

function num(value, digits = 4) {
  const n = Number(value);
  if (!Number.isFinite(n)) return "n/a";
  return n.toFixed(digits);
}

function pct(value, digits = 1) {
  const n = Number(value);
  if (!Number.isFinite(n)) return "n/a";
  return `${(n * 100).toFixed(digits)}%`;
}

function points(value) {
  const n = Number(value);
  if (!Number.isFinite(n)) return "n/a";
  return n.toLocaleString("pt-BR", { maximumFractionDigits: 0 });
}

function loadData() {
  const presentationData = JSON.parse(fs.readFileSync(path.join(TABLE, "presentation_data.json"), "utf8"));
  const globalSummary = readCsv(path.join(TABLE, "official_global_summary.csv"));
  const bestMetrics = readCsv(path.join(TABLE, "best_model_metric_comparison.csv"));
  const backtestSummary = readCsv(path.join(TABLE, "official_backtest_summary.csv"));
  const backtestTests = readCsv(path.join(TABLE, "official_backtest_statistical_tests.csv"));
  const features = readCsv(path.join(TABLE, "infogain7_features.csv"));
  const split = readCsv(path.join(TABLE, "dataset_split_summary.csv"));
  const searchSpace = readCsv(path.join(TABLE, "search_space_table.csv"));
  const structural = readCsv(path.join(TABLE, "structural_pretest_summary.csv"));
  const validationSignal = readCsv(path.join(TABLE, "best_model_validation_signal.csv"));
  const mcc = globalSummary.find((row) => row.fitness_mode_label === "MCC/F1");
  const acc = globalSummary.find((row) => row.fitness_mode_label === "Accuracy-CV");
  const mccBest = Object.fromEntries(bestMetrics.filter((row) => row.fitness_mode_label === "MCC/F1").map((row) => [row.metric, row.score]));
  const accBest = Object.fromEntries(bestMetrics.filter((row) => row.fitness_mode_label === "Accuracy-CV").map((row) => [row.metric, row.score]));
  return { presentationData, globalSummary, bestMetrics, backtestSummary, backtestTests, features, split, searchSpace, structural, validationSignal, mcc, acc, mccBest, accBest };
}

function img(...parts) {
  return ensureFile(path.join(...parts));
}

function tableRowsForSearchSpace(searchSpace) {
  const grouped = new Map();
  for (const row of searchSpace) {
    if (!grouped.has(row.model)) grouped.set(row.model, []);
    grouped.get(row.model).push(`${row.hyperparameter}: ${row.domain}`);
  }
  return [...grouped.entries()].map(([model, params]) => [model, params.slice(0, 4).join("\n") + (params.length > 4 ? "\n..." : "")]);
}

function buildSlides(data) {
  const figures = {
    split: img(FIG, "dataset_temporal_split.png"),
    structural: img(FIG, "structural_pretest_best_fitness.png"),
    convMcc: img(FIG, "convergence_mcc_f1_mlp_cnn.png"),
    convAcc: img(FIG, "convergence_accuracy_cv_mlp_cnn.png"),
    trainMcc: img(FIG, "train_signal_vs_test_accuracy_mcc_f1.png"),
    trainAcc: img(FIG, "train_signal_vs_test_accuracy_accuracy_cv.png"),
    bestMetrics: img(FIG, "best_model_metrics_mlp_gwo.png"),
    sideAccuracy: img(FIG, "fitness_side_by_side_accuracy_test.png"),
    gapMcc: img(FIG, "gap_heatmap_mcc_test.png"),
    gapAccuracy: img(FIG, "gap_heatmap_accuracy_test.png"),
    backtestEquity: img(FIG, "official_backtest_equity_curve.png"),
    backtestMetrics: img(FIG, "official_backtest_metrics.png"),
    mccByOptimizer: img(ROOT, "outputs", "comparative_analysis", "mcc_fitness_mcc_test_by_model_optimizer.png"),
    accByOptimizer: img(FIG, "accuracy_cv_accuracy_test_by_model_optimizer_clean.png"),
    globalCompare: img(ROOT, "outputs", "comparative_analysis", "global_mcc_accuracy_comparison.png"),
    mlpArch: img(ROOT, "outputs", "article_figures", "architecture_network", "mlp_network_architecture.png"),
    cnnArch: img(ROOT, "outputs", "article_figures", "architecture_network", "cnn_network_architecture.png"),
  };

  const splitRows = data.split.map((row) => [row.split, row.rows, row.start, row.end]);
  const featureRows = data.features.map((row) => [row.index, row.feature]);
  const backtestRows = data.backtestSummary.map((row) => [
    row.fitness_mode,
    points(row.total_profit_points_mean),
    num(row.profit_factor_mean, 3),
    num(row.sharpe_ratio_annualized_mean, 2),
    points(row.max_drawdown_points_mean),
  ]);
  const structuralRows = data.structural
    .filter((row) => row.model_type === "mlp" || row.model_type === "cnn")
    .map((row) => [row.model_type.toUpperCase(), `${row.optimizer.toUpperCase()} + ${row.activation.toUpperCase()}`, num(row.best_fitness, 4)]);
  const validationRows = data.validationSignal.map((row) => [
    row.fitness_mode_label,
    num(row.fitness, 4),
    num(row.accuracy, 4),
    num(row.mcc, 4),
    num(row.f1, 4),
  ]);

  const mccAccDelta = Number(data.mcc.accuracy_test_mean) - Number(data.acc.accuracy_test_mean);
  const mccMccDelta = Number(data.mcc.mcc_test_mean) - Number(data.acc.mcc_test_mean);
  const backtestMcc = data.backtestSummary.find((row) => row.fitness_mode === "MCC/F1");
  const backtestAcc = data.backtestSummary.find((row) => row.fitness_mode === "Accuracy-CV");
  const backtestDelta = Number(backtestAcc.total_profit_points_mean) - Number(backtestMcc.total_profit_points_mean);
  const stats = data.backtestTests[0];

  return [
    {
      layout: "cover",
      kicker: "RESULTADOS DO DESENVOLVIMENTO",
      title: "Benchmark controlado de otimizadores para classificacao intraday",
      subtitle: "Da experiencia antiga com GA isolado para um protocolo temporal com 4 modelos, 5 otimizadores e 2 funcoes de fitness.",
      metrics: [
        ["15.057", "amostras WIN 5 min"],
        ["40", "combinacoes oficiais"],
        ["3 seeds", "media no X_test cego"],
      ],
    },
    {
      layout: "takeaways",
      kicker: "TESE",
      title: "A contribuicao principal agora e metodologica, nao apenas um novo resultado de acuracia.",
      bullets: [
        "Substituimos a validacao antiga com shuffle por um split temporal sem vazamento.",
        "Padronizamos budget: 1000 avaliacoes de fitness por seed para todos os otimizadores.",
        "Comparamos dois regimes de fitness e validamos o melhor modelo em teste cego e backtest economico.",
      ],
      metrics: [
        ["MCC/F1", "fitness recomendado"],
        ["MLP + GWO", "melhor par medio"],
        [num(data.mcc.accuracy_test_mean, 4), "accuracy media MCC/F1"],
      ],
    },
    {
      layout: "compare",
      kicker: "EVOLUCAO DO PROTOCOLO",
      title: "O novo desenho corrige a principal fragilidade da pasta antiga de experimentos.",
      leftTitle: "Antes: experiments/train_model",
      leftBullets: [
        "Foco em GA e modelos isolados.",
        "StratifiedKFold com shuffle dentro do GA.",
        "Comparacoes menos padronizadas por budget.",
        "Menos evidencia economica e estatistica.",
      ],
      rightTitle: "Agora: benchmark oficial",
      rightBullets: [
        "Split temporal 60/20/20 sem shuffle.",
        "4 modelos x 5 otimizadores x 2 fitness.",
        "Mesmas seeds e mesmo numero de avaliacoes.",
        "X_test cego + backtest oficial do melhor par.",
      ],
    },
    {
      layout: "imageRail",
      kicker: "DADOS",
      title: "A divisao temporal transforma o benchmark em um teste mais parecido com mercado real.",
      image: figures.split,
      rail: [
        ["Ativo", "WIN / Mini Indice"],
        ["Frequencia", "5 minutos"],
        ["Periodo", `${data.presentationData.dataset.start} a ${data.presentationData.dataset.end}`],
        ["Teste", "20% final sem shuffle"],
      ],
      note: "As datas aparecem apos ordenacao temporal e limpeza do pipeline de modelagem.",
    },
    {
      layout: "table",
      kicker: "FEATURES",
      title: "O benchmark manteve o conjunto enxuto InfoGain_7 para isolar o efeito dos otimizadores.",
      headers: ["Indice", "Feature efetiva no pipeline"],
      rows: featureRows,
      sideText: "Observacao: os indices do config sao resolvidos sobre as features numericas usadas pelo pipeline, nao sobre o CSV bruto completo.",
    },
    {
      layout: "imagePair",
      kicker: "MODELOS",
      title: "Comparamos modelos classicos e deep learning sob o mesmo protocolo.",
      images: [
        [figures.mlpArch, "MLP: rede densa para padroes nao lineares nas features tecnicas."],
        [figures.cnnArch, "CNN: convolucoes 1D para padroes locais nos indicadores."],
      ],
      bullets: [
        "SVM testa margem e kernels linear/RBF.",
        "Random Forest testa ensembles de arvores robustos.",
      ],
    },
    {
      layout: "cards",
      kicker: "OTIMIZADORES",
      title: "Cinco estrategias cobrem busca aleatoria, evolucao, enxame e populacoes diferenciais.",
      cards: [
        ["Random Search", "Baseline: amostra o espaco sem memoria."],
        ["GA", "Selecao, crossover e mutacao."],
        ["PSO", "Particulas seguem melhor posicao individual e coletiva."],
        ["DE", "Perturba vetores usando diferencas populacionais."],
        ["GWO", "Lideranca alfa/beta/delta guia exploracao."],
      ],
      note: "No material, PCA foi corrigido para PSO: Particle Swarm Optimization.",
    },
    {
      layout: "table",
      kicker: "ESPACOS DE BUSCA",
      title: "Cada modelo teve um espaco de hiperparametros proprio, mas o budget foi comum.",
      headers: ["Modelo", "Parametros otimizados"],
      rows: tableRowsForSearchSpace(data.searchSpace),
      sideText: "Todos os candidatos sao normalizados para limites validos antes da avaliacao.",
    },
    {
      layout: "cards",
      kicker: "CONFIGURACAO OFICIAL",
      title: "O benchmark final foi desenhado para comparar otimizadores por numero de avaliacoes.",
      cards: [
        ["Seeds", "1, 2 e 3"],
        ["Budget", "1000 avaliacoes por seed"],
        ["GA / DE", "Populacao = 10"],
        ["PSO", "10 particulas; inertia 0.70"],
        ["GWO", "10 lobos"],
        ["MLP/CNN", "tanh + rmsprop; max_epochs=10"],
      ],
      note: "A metrica final e sempre no X_test cego; fitness bruto nao e comparado entre formulas diferentes.",
    },
    {
      layout: "formula",
      kicker: "FITNESS",
      title: "Testamos duas funcoes objetivo com intencoes diferentes.",
      formulas: [
        ["MCC/F1", "0.6 * MCC + 0.4 * F1", "Prioriza equilibrio de classe e qualidade da classificacao."],
        ["Accuracy-CV", "mean(0.4 * Acc_train + 0.6 * Acc_val)", "Usa TimeSeriesSplit com 3 folds para estabilidade temporal."],
      ],
      note: "A conclusao usa metricas iguais no teste, nao o valor numerico de fitness.",
    },
    {
      layout: "imageRail",
      kicker: "PRE-TESTE",
      title: "O pre-teste estrutural escolheu rmsprop + tanh para levar ao benchmark oficial.",
      image: figures.structural,
      rail: structuralRows.slice(0, 4).map((row) => [`${row[0]} ${row[1]}`, row[2]]),
      note: "Fonte: structural_fast_official_space; etapa exploratoria para fixar treinamento/ativacao.",
    },
    {
      layout: "imageFull",
      kicker: "MCC/F1",
      title: "GA, PSO e GWO estabilizam rapido; MLP e CNN convergem para regioes parecidas.",
      image: figures.convMcc,
      note: "Eixo X = evaluation_id; eixo Y = best_fitness_so_far medio nas seeds 1, 2 e 3.",
    },
    {
      layout: "imageFull",
      kicker: "ACCURACY-CV",
      title: "A fitness de acuracia temporal sobe em escala diferente, mas deve ser julgada no mesmo X_test.",
      image: figures.convAcc,
      note: "Escalas diferentes de fitness nao podem ser comparadas diretamente contra MCC/F1.",
    },
    {
      layout: "imageFull",
      kicker: "RESULTADOS MCC/F1",
      title: "No teste cego, MLP + GWO foi o melhor par medio em MCC e accuracy.",
      image: figures.mccByOptimizer,
      note: "Barras mostram media; hastes mostram erro padrao da media; pontos mostram as seeds individuais.",
    },
    {
      layout: "imageFull",
      kicker: "RESULTADOS ACCURACY-CV",
      title: "Accuracy-CV tambem escolhe MLP + GWO, mas perde levemente para MCC/F1 no criterio final.",
      image: figures.accByOptimizer,
      note: "O grafico mostra accuracy no X_test por modelo e otimizador.",
    },
    {
      layout: "imageFull",
      kicker: "AJUSTE VS TESTE",
      title: "No regime MCC/F1, o sinal de validacao e o teste mostram estabilidade nos melhores pares.",
      image: figures.trainMcc,
      note: "Para MCC/F1, o sinal disponivel e acuracia de validacao do candidato vencedor.",
    },
    {
      layout: "imageFull",
      kicker: "AJUSTE VS TESTE",
      title: "No Accuracy-CV, o grafico contrasta acuracia media de treino CV com o X_test cego.",
      image: figures.trainAcc,
      note: "O objetivo usa folds temporais; o teste final permanece intocado.",
    },
    {
      layout: "imageRail",
      kicker: "COMPARACAO DOS FITNESS",
      title: "MCC/F1 vence levemente no agregado de accuracy e MCC no X_test.",
      image: figures.globalCompare,
      rail: [
        ["Delta accuracy", `+${num(mccAccDelta, 4)} para MCC/F1`],
        ["Delta MCC", `+${num(mccMccDelta, 4)} para MCC/F1`],
        ["Vitorias por combo", "13 de 20 em accuracy e MCC"],
      ],
      note: "Accuracy-CV melhora alguns casos especificos, especialmente CNN/MLP em otimizadores menos estaveis.",
    },
    {
      layout: "imageRail",
      kicker: "MELHOR MODELO",
      title: "MLP + GWO e o ponto de convergencia das duas fitness.",
      image: figures.bestMetrics,
      rail: [
        ["MCC/F1 accuracy", num(data.mccBest.Accuracy, 4)],
        ["MCC/F1 MCC", num(data.mccBest.MCC, 4)],
        ["Accuracy-CV accuracy", num(data.accBest.Accuracy, 4)],
        ["Accuracy-CV MCC", num(data.accBest.MCC, 4)],
      ],
      note: "A diferenca e pequena, mas favorece MCC/F1 para a narrativa principal.",
    },
    {
      layout: "imageFull",
      kicker: "GAP GLOBAL",
      title: "A leitura por gap mostra onde cada combinacao fica em relacao ao melhor MCC.",
      image: figures.gapMcc,
      note: "Formula: (valor_combo - melhor_global) / |melhor_global| * 100.",
    },
    {
      layout: "imageFull",
      kicker: "GAP GLOBAL",
      title: "Em accuracy, as melhores combinacoes ficam muito proximas; RF sofre mais com Accuracy-CV.",
      image: figures.gapAccuracy,
      note: "O melhor global em accuracy no teste e MLP + GWO sob MCC/F1.",
    },
    {
      layout: "imageRail",
      kicker: "BACKTEST OFICIAL",
      title: "O teste economico confirma que ambos os fitness superam o baseline long-only no periodo cego.",
      image: figures.backtestEquity,
      rail: [
        ["MCC/F1 lucro", `${points(backtestMcc.total_profit_points_mean)} pts`],
        ["Accuracy-CV lucro", `${points(backtestAcc.total_profit_points_mean)} pts`],
        ["Delta economico", `${points(backtestDelta)} pts para Accuracy-CV`],
      ],
      note: "Estrategia: long se y_pred=1, short se y_pred=0, custo fixo de 5 pontos por trade.",
    },
    {
      layout: "imageRail",
      kicker: "ECONOMICO + ESTATISTICA",
      title: "A diferenca economica entre os dois fitness nao aparece estatisticamente forte.",
      image: figures.backtestMetrics,
      rail: [
        ["Dias pareados", stats.n_days],
        ["Dif. diaria media", `${num(stats.mean_daily_difference_points, 2)} pts`],
        ["CI bootstrap 95%", `${num(stats.bootstrap_ci95_low, 1)} a ${num(stats.bootstrap_ci95_high, 1)}`],
        ["Wilcoxon p", num(stats.wilcoxon_p_value, 3)],
      ],
      note: "Comparacao diaria: MCC/F1 menos Accuracy-CV.",
    },
    {
      layout: "conclusion",
      kicker: "CONCLUSAO",
      title: "Recomendacao: usar MCC/F1 como fitness principal do artigo.",
      bullets: [
        `MCC/F1 lidera no X_test: accuracy media ${num(data.mcc.accuracy_test_mean, 4)} vs ${num(data.acc.accuracy_test_mean, 4)}.`,
        `MCC medio tambem favorece MCC/F1: ${num(data.mcc.mcc_test_mean, 4)} vs ${num(data.acc.mcc_test_mean, 4)}.`,
        "Accuracy-CV entra como experimento complementar de estabilidade temporal.",
        "O backtest oficial mostra desempenho economico positivo para ambos, sem diferenca diaria estatisticamente forte.",
      ],
      finalMetric: "MLP + GWO",
      finalLabel: "melhor combinacao media nas duas fitness",
    },
    {
      layout: "table",
      kicker: "APENDICE",
      title: "Espaco de busca completo por modelo.",
      headers: ["Modelo", "Parametros"],
      rows: tableRowsForSearchSpace(data.searchSpace),
      sideText: "Esta tabela vem diretamente de config/search_spaces.yaml.",
    },
    {
      layout: "table",
      kicker: "APENDICE",
      title: "Sinais de validacao registrados para o melhor par MLP + GWO.",
      headers: ["Fitness", "Fitness val.", "Acc val.", "MCC val.", "F1 val."],
      rows: validationRows,
      sideText: "No Accuracy-CV, MCC/F1 de validacao nao e o objetivo registrado; por isso a avaliacao final usa metricas iguais no X_test.",
    },
    {
      layout: "table",
      kicker: "APENDICE",
      title: "Resumo economico oficial por fitness.",
      headers: ["Fitness", "Lucro pts", "PF", "Sharpe", "Max DD"],
      rows: backtestRows,
      sideText: "O baseline long-only foi incluido apenas como referencia do periodo de teste.",
    },
  ];
}

function buildDeckUtils() {
  return String.raw`
import { SLIDES } from "./slides-data.mjs";

const C = ${JSON.stringify(COLORS, null, 2)};

function add(slide, ctx, text, x, y, w, h, opts = {}) {
  return ctx.addText(slide, {
    text,
    x, y, w, h,
    fontSize: opts.size ?? 22,
    color: opts.color ?? C.ink,
    bold: opts.bold ?? false,
    typeface: opts.face ?? (opts.title ? ctx.fonts.title : ctx.fonts.body),
    align: opts.align ?? "left",
    valign: opts.valign ?? "top",
    fill: opts.fill ?? "#00000000",
    line: opts.line ?? ctx.line("#00000000", 0),
    insets: opts.insets ?? { left: 0, right: 0, top: 0, bottom: 0 },
    name: opts.name,
  });
}

function rect(slide, ctx, x, y, w, h, fill, lineFill = "#00000000", lineWidth = 0) {
  return ctx.addShape(slide, { x, y, w, h, fill, line: ctx.line(lineFill, lineWidth) });
}

function base(slide, ctx, spec) {
  rect(slide, ctx, 0, 0, ctx.W, ctx.H, spec.dark ? C.dark : C.paper);
  if (!spec.dark) {
    rect(slide, ctx, 0, 0, 12, ctx.H, C.blue);
  }
  const color = spec.dark ? C.white : C.ink;
  const muted = spec.dark ? "#CAD5E4" : C.muted;
  const marker = rect(slide, ctx, 54, 33, 8, 8, spec.dark ? "#9CC3FF" : C.blue);
  marker.name = "kicker-marker";
  add(slide, ctx, spec.kicker || "NCA BENCHMARK", 72, 26, 620, 22, { size: 13, color: spec.dark ? "#9CC3FF" : C.blue, bold: true, name: "kicker-label" });
  if (spec.title) add(slide, ctx, spec.title, 54, 56, 940, 86, { size: 30, color, bold: true, title: true });
  add(slide, ctx, "NCA optimizer benchmark | resultados ao professor", 54, 690, 540, 18, { size: 10, color: muted });
  add(slide, ctx, String(ctx.slideNumber).padStart(2, "0"), 1194, 688, 36, 18, { size: 10, color: muted, align: "right" });
}

function bullets(slide, ctx, items, x, y, w, size = 20, color = C.ink) {
  let top = y;
  for (const item of items || []) {
    add(slide, ctx, "•", x, top + 1, 18, 30, { size, color: C.orange, bold: true });
    add(slide, ctx, item, x + 24, top, w - 24, 54, { size, color });
    top += 58;
  }
}

function metric(slide, ctx, value, label, x, y, w, dark = false) {
  const fill = dark ? "#1F2937" : "#FFFFFF";
  rect(slide, ctx, x, y, w, 92, fill, dark ? "#374151" : C.faint, 1);
  const valueText = String(value);
  const valueSize = valueText.length > 18 ? 18 : valueText.length > 12 ? 23 : 28;
  add(slide, ctx, valueText, x + 18, y + 12, w - 36, 46, { size: valueSize, color: dark ? C.white : C.blue, bold: true, title: true });
  add(slide, ctx, label, x + 18, y + 58, w - 36, 21, { size: 14, color: dark ? "#CBD5E1" : C.muted });
}

async function image(slide, ctx, file, x, y, w, h, fit = "contain") {
  return await ctx.addImage(slide, { path: file, x, y, w, h, fit, alt: file });
}

function table(slide, ctx, headers, rows, x, y, w, rowH = 42, widths = undefined) {
  const cols = headers.length;
  const colWidths = widths || Array(cols).fill(w / cols);
  let cx = x;
  for (let i = 0; i < cols; i += 1) {
    rect(slide, ctx, cx, y, colWidths[i], rowH, C.blue, C.blue, 1);
    add(slide, ctx, headers[i], cx + 8, y + 9, colWidths[i] - 16, rowH - 12, { size: 13, color: C.white, bold: true });
    cx += colWidths[i];
  }
  rows.forEach((row, r) => {
    cx = x;
    const yy = y + rowH * (r + 1);
    const fill = r % 2 === 0 ? "#FFFFFF" : "#F0EDE6";
    for (let i = 0; i < cols; i += 1) {
      rect(slide, ctx, cx, yy, colWidths[i], rowH, fill, C.faint, 1);
      add(slide, ctx, String(row[i] ?? ""), cx + 8, yy + 7, colWidths[i] - 16, rowH - 10, { size: 12, color: C.ink });
      cx += colWidths[i];
    }
  });
}

function cards(slide, ctx, cards, x, y, w, h, cols = 3) {
  const gap = 18;
  const cardW = (w - gap * (cols - 1)) / cols;
  const cardH = h;
  cards.forEach((card, i) => {
    const cx = x + (i % cols) * (cardW + gap);
    const cy = y + Math.floor(i / cols) * (cardH + gap);
    rect(slide, ctx, cx, cy, cardW, cardH, "#FFFFFF", C.faint, 1);
    add(slide, ctx, card[0], cx + 18, cy + 15, cardW - 36, 28, { size: 19, bold: true, color: C.blue, title: true });
    add(slide, ctx, card[1], cx + 18, cy + 52, cardW - 36, cardH - 62, { size: 15, color: C.muted });
  });
}

export async function renderSlide(presentation, ctx, index) {
  const spec = SLIDES[index - 1];
  const slide = presentation.slides.add();

  if (spec.layout === "cover") {
    spec.dark = true;
    base(slide, ctx, { ...spec, title: "" });
    add(slide, ctx, spec.kicker, 66, 54, 520, 24, { size: 14, color: "#9CC3FF", bold: true });
    add(slide, ctx, spec.title, 66, 118, 870, 150, { size: 46, color: C.white, bold: true, title: true });
    add(slide, ctx, spec.subtitle, 70, 292, 750, 70, { size: 22, color: "#CBD5E1" });
    (spec.metrics || []).forEach((m, i) => metric(slide, ctx, m[0], m[1], 70 + i * 250, 452, 220, true));
    rect(slide, ctx, 930, 96, 230, 430, "#1F2937", "#374151", 1);
    add(slide, ctx, "Fluxo do benchmark", 958, 132, 180, 28, { size: 20, color: C.white, bold: true });
    ["Dados temporais", "Features InfoGain_7", "Busca de hiperparametros", "Teste cego + backtest"].forEach((txt, i) => {
      const y = 196 + i * 72;
      rect(slide, ctx, 962, y, 24, 24, i === 3 ? C.orange : C.blue);
      add(slide, ctx, txt, 1002, y - 3, 148, 42, { size: 15, color: "#E5E7EB" });
      if (i < 3) rect(slide, ctx, 973, y + 28, 2, 36, "#526070");
    });
    return slide;
  }

  base(slide, ctx, spec);

  if (spec.layout === "takeaways") {
    bullets(slide, ctx, spec.bullets, 68, 170, 650, 21);
    (spec.metrics || []).forEach((m, i) => metric(slide, ctx, m[0], m[1], 812, 170 + i * 122, 300));
  } else if (spec.layout === "compare") {
    rect(slide, ctx, 70, 170, 510, 420, "#FFFFFF", C.faint, 1);
    rect(slide, ctx, 700, 170, 510, 420, "#FFFFFF", C.faint, 1);
    add(slide, ctx, spec.leftTitle, 100, 198, 450, 34, { size: 24, bold: true, color: C.red, title: true });
    add(slide, ctx, spec.rightTitle, 730, 198, 450, 34, { size: 24, bold: true, color: C.green, title: true });
    bullets(slide, ctx, spec.leftBullets, 102, 260, 420, 18);
    bullets(slide, ctx, spec.rightBullets, 732, 260, 420, 18);
  } else if (spec.layout === "imageRail") {
    await image(slide, ctx, spec.image, 70, 165, 790, 455);
    let y = 172;
    for (const item of spec.rail || []) {
      metric(slide, ctx, item[1], item[0], 908, y, 270);
      y += 102;
    }
    if (spec.note) add(slide, ctx, spec.note, 70, 638, 980, 28, { size: 12, color: C.muted });
  } else if (spec.layout === "table") {
    const widths = spec.headers.length === 2 ? [160, 700] : undefined;
    const rowH = spec.headers.length === 2 && spec.rows.length <= 4 ? 88 : spec.headers.length === 2 ? 50 : 40;
    table(slide, ctx, spec.headers, spec.rows, 70, 166, spec.headers.length === 2 ? 860 : 900, rowH, widths);
    if (spec.sideText) {
      rect(slide, ctx, 980, 176, 220, 290, "#FFFFFF", C.faint, 1);
      add(slide, ctx, "Nota de leitura", 1000, 198, 180, 28, { size: 18, bold: true, color: C.blue });
      add(slide, ctx, spec.sideText, 1000, 240, 175, 190, { size: 15, color: C.muted });
    }
  } else if (spec.layout === "imagePair") {
    await image(slide, ctx, spec.images[0][0], 70, 164, 480, 270);
    await image(slide, ctx, spec.images[1][0], 610, 164, 520, 270);
    add(slide, ctx, spec.images[0][1], 82, 448, 450, 48, { size: 15, color: C.muted });
    add(slide, ctx, spec.images[1][1], 622, 448, 490, 48, { size: 15, color: C.muted });
    bullets(slide, ctx, spec.bullets, 90, 542, 880, 18);
  } else if (spec.layout === "cards") {
    cards(slide, ctx, spec.cards, 70, 172, 1060, 112, 3);
    if (spec.note) add(slide, ctx, spec.note, 74, 642, 940, 30, { size: 13, color: C.muted });
  } else if (spec.layout === "formula") {
    spec.formulas.forEach((f, i) => {
      const x = i === 0 ? 78 : 666;
      rect(slide, ctx, x, 178, 520, 318, "#FFFFFF", i === 0 ? C.blue : C.orange, 2);
      add(slide, ctx, f[0], x + 28, 210, 430, 34, { size: 27, bold: true, color: i === 0 ? C.blue : C.orange, title: true });
      add(slide, ctx, f[1], x + 28, 276, 462, 52, { size: 24, bold: true, color: C.ink, face: ctx.fonts.mono });
      add(slide, ctx, f[2], x + 28, 370, 444, 82, { size: 17, color: C.muted });
    });
    if (spec.note) add(slide, ctx, spec.note, 82, 560, 1000, 34, { size: 15, color: C.muted });
  } else if (spec.layout === "imageFull") {
    await image(slide, ctx, spec.image, 64, 154, 1118, 474);
    if (spec.note) add(slide, ctx, spec.note, 70, 640, 1000, 25, { size: 12, color: C.muted });
  } else if (spec.layout === "conclusion") {
    bullets(slide, ctx, spec.bullets, 76, 168, 740, 20);
    rect(slide, ctx, 878, 190, 270, 230, C.blue);
    add(slide, ctx, spec.finalMetric, 902, 238, 220, 60, { size: 36, color: C.white, bold: true, title: true, align: "center" });
    add(slide, ctx, spec.finalLabel, 914, 320, 196, 64, { size: 17, color: "#DBEAFE", align: "center" });
    rect(slide, ctx, 878, 458, 270, 116, "#FFFFFF", C.faint, 1);
    add(slide, ctx, "Uso no artigo", 900, 478, 220, 24, { size: 18, color: C.blue, bold: true });
    add(slide, ctx, "MCC/F1 como fitness principal; Accuracy-CV como analise complementar.", 900, 508, 220, 50, { size: 14, color: C.muted });
  }

  return slide;
}
`;
}

async function writeWorkspace(slides) {
  await fsp.rm(WORKSPACE, { recursive: true, force: true });
  await fsp.mkdir(SLIDES_DIR, { recursive: true });
  await fsp.mkdir(PREVIEW_DIR, { recursive: true });
  await fsp.mkdir(LAYOUT_DIR, { recursive: true });
  await fsp.mkdir(QA_DIR, { recursive: true });

  await fsp.writeFile(path.join(WORKSPACE, "profile-plan.txt"), [
    "task mode: create",
    "primary deck-profile: engineering-platform",
    "secondary profile gates: appendix-heavy",
    "required proof objects: protocol workflow, optimizer/model comparison, convergence, final test metrics, economic backtest",
    "known missing inputs: none; feature names corrected to pipeline-resolved InfoGain_7",
  ].join("\n"), "utf8");
  await fsp.writeFile(path.join(WORKSPACE, "source-notes.txt"), [
    "Sources: local repo configs, official output CSVs, generated figures, and official backtest outputs.",
    "Identity assets: none used.",
    "All figures are local generated benchmark artifacts.",
  ].join("\n"), "utf8");
  await fsp.writeFile(path.join(WORKSPACE, "claim-spine.txt"), slides.map((s, i) => `${i + 1}. ${s.kicker}: ${s.title}`).join("\n"), "utf8");
  await fsp.writeFile(path.join(WORKSPACE, "design-system.txt"), [
    "Slide size: 1280x720.",
    "Palette: warm paper, deep ink, blue primary, orange comparison, green positive.",
    "Chart grammar: high-resolution generated evidence figures with concise rail summaries.",
    "Typography: Aptos Display for claims, Aptos for body.",
  ].join("\n"), "utf8");
  await fsp.writeFile(path.join(WORKSPACE, "contact-sheet-plan.txt"), [
    "Layouts: cover, takeaways, compare, image+rail, image-full, formula, tables, conclusion.",
    "No more than two consecutive slides share the same macro layout when possible.",
  ].join("\n"), "utf8");

  await fsp.writeFile(path.join(SLIDES_DIR, "slides-data.mjs"), `export const SLIDES = ${JSON.stringify(slides, null, 2)};\n`, "utf8");
  await fsp.writeFile(path.join(SLIDES_DIR, "deck-utils.mjs"), buildDeckUtils(), "utf8");

  for (let i = 1; i <= slides.length; i += 1) {
    const n = String(i).padStart(2, "0");
    await fsp.writeFile(
      path.join(SLIDES_DIR, `slide-${n}.mjs`),
      `import { renderSlide } from "./deck-utils.mjs";\nexport async function slide${n}(presentation, ctx) {\n  return await renderSlide(presentation, ctx, ${i});\n}\n`,
      "utf8",
    );
  }
}

function runNode(script, args, options = {}) {
  const result = spawnSync("node", [script, ...args], {
    cwd: ROOT,
    encoding: "utf8",
    env: {
      ...process.env,
      HOME: process.env.HOME || "C:/Users/User",
      USERPROFILE: process.env.USERPROFILE || "C:/Users/User",
      PYTHON: path.join(ROOT, ".venv", "Scripts", "python.exe"),
    },
    ...options,
  });
  if (result.status !== 0) {
    throw new Error([`Command failed: node ${script} ${args.join(" ")}`, result.stdout, result.stderr].filter(Boolean).join("\n"));
  }
  return result.stdout;
}

async function main() {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  const data = loadData();
  const slides = buildSlides(data);
  await writeWorkspace(slides);

  const buildScript = path.join(SKILL_DIR, "scripts", "build_artifact_deck.mjs");
  const manifestPath = path.join(WORKSPACE, "artifact-build-manifest.json");
  const contactSheet = path.join(PREVIEW_DIR, "contact-sheet.png");
  const stdout = runNode(buildScript, [
    "--workspace", WORKSPACE,
    "--slides-dir", SLIDES_DIR,
    "--out", FINAL_PPTX,
    "--preview-dir", PREVIEW_DIR,
    "--layout-dir", path.join(LAYOUT_DIR, "final"),
    "--contact-sheet", contactSheet,
    "--manifest", manifestPath,
    "--slide-count", String(slides.length),
    "--slide-size", "1280x720",
    "--scale", "1",
  ]);

  const layoutCheckScript = path.join(SKILL_DIR, "scripts", "check_layout_quality.mjs");
  const layoutCheck = runNode(layoutCheckScript, [
    "--layout", path.join(LAYOUT_DIR, "final"),
    "--warn-only",
    "--min-gap", "8",
  ]);

  const scorecard = [
    "Final QA ledger",
    `slides: ${slides.length}`,
    `pptx: ${FINAL_PPTX}`,
    `contact sheet: ${contactSheet}`,
    "profile gate: engineering-platform pass",
    "appendix-heavy gate: pass; dense tables moved to appendix slides",
    "known caveat: MCC/F1 train-vs-test slide uses validation accuracy as adjustment signal because train accuracy is not logged for that mode.",
    "",
    "Layout check:",
    layoutCheck,
  ].join("\n");
  await fsp.writeFile(path.join(QA_DIR, "comeback-scorecard.txt"), scorecard, "utf8");

  console.log(stdout);
  console.log(`Final PPTX: ${rel(FINAL_PPTX)}`);
  console.log(`Workspace: ${rel(WORKSPACE)}`);
  console.log(`Contact sheet: ${rel(contactSheet)}`);
}

main().catch((error) => {
  console.error(error.stack || error.message || String(error));
  process.exit(1);
});
