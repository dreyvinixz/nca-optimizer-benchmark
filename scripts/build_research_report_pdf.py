#!/usr/bin/env python3
"""Build a Portuguese technical report PDF from the frozen study summaries."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
    Spacer, Table, TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
CHART_DIR = ROOT / "tmp" / "pdfs"
OUT = ROOT / "output" / "pdf" / "relatorio_tecnico_rotulos_intradiarios_b0.pdf"

NAVY = colors.HexColor("#17324D")
TEAL = colors.HexColor("#117C78")
ORANGE = colors.HexColor("#E78335")
PALE = colors.HexColor("#EFF5F7")
MID = colors.HexColor("#5A6B78")
INK = colors.HexColor("#1E2933")
GRID = colors.HexColor("#D6E0E5")


def setup_fonts():
    font_root = Path("C:/Windows/Fonts")
    pdfmetrics.registerFont(TTFont("Arial", str(font_root / "arial.ttf")))
    pdfmetrics.registerFont(TTFont("Arial-Bold", str(font_root / "arialbd.ttf")))
    pdfmetrics.registerFont(TTFont("Arial-Italic", str(font_root / "ariali.ttf")))
    pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold", italic="Arial-Italic", boldItalic="Arial-Bold")


def load_data():
    metrics = pd.read_csv(REPORTS / "final_test_metrics.csv")
    test = metrics[(metrics.split == "test") & (metrics.root == "ALL") & (metrics.test_block.astype(str) == "overall")].copy()
    test = test.set_index(["model", "target"])
    trainval = pd.read_csv(REPORTS / "overfitting_train_validation.csv")
    sessions = pd.read_csv(REPORTS / "overfitting_session_metrics.csv")
    paired = pd.read_csv(REPORTS / "final_test_metrics.csv")
    cv = pd.read_csv(REPORTS / "mlp_cv_summary.csv")
    contracts = pd.read_csv(REPORTS / "final_test_contract_metrics.csv")
    return test, trainval, sessions, paired, cv, contracts


def make_charts(test, trainval, sessions):
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    model_order = ["hist_gradient_boosting", "independent_mlp", "shared_multitask_mlp"]
    model_labels = ["HistGradientBoosting", "MLP independente", "MLP compartilhado"]
    target_order = ["trend_5m", "trend_10m", "trend_15m"]
    target_labels = ["5 min", "10 min", "15 min"]
    palette = ["#117C78", "#17324D", "#E78335"]

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.1))
    for ax, metric, title, ylim in [
        (axes[0], "mcc", "MCC no teste", (0.35, 0.55)),
        (axes[1], "roc_auc", "ROC-AUC no teste", (0.70, 0.90)),
    ]:
        x = np.arange(3)
        width = 0.23
        for j, (model, label, color) in enumerate(zip(model_order, model_labels, palette)):
            vals = [test.loc[(model, target), metric] for target in target_order]
            ax.bar(x + (j - 1) * width, vals, width, label=label, color=color)
        ax.set_title(title, fontsize=12, fontweight="bold", color="#17324D")
        ax.set_xticks(x, target_labels)
        ax.set_ylim(*ylim)
        ax.grid(axis="y", color="#D6E0E5", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.tick_params(axis="y", labelsize=8, length=0)
        ax.tick_params(axis="x", labelsize=9, length=0)
    axes[0].set_ylabel("Pontuacao", fontsize=9)
    axes[1].legend(loc="lower center", bbox_to_anchor=(-0.05, -0.31), ncol=3, frameon=False, fontsize=8)
    fig.tight_layout(rect=(0, 0.10, 1, 1))
    chart_mcc_auc = CHART_DIR / "mcc_roc_auc.png"
    fig.savefig(chart_mcc_auc, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.1))
    for ax, metric, title in [
        (axes[0], "mcc_gap_train_minus_validation", "Gap MCC aparente: treino menos validacao"),
        (axes[1], "brier_gap_validation_minus_train", "Gap Brier: validacao menos treino"),
    ]:
        x = np.arange(3)
        width = 0.23
        for j, (model, label, color) in enumerate(zip(model_order, model_labels, palette)):
            g = trainval[trainval.model == model].set_index("target")
            vals = [g.loc[t, metric] for t in target_order]
            ax.bar(x + (j - 1) * width, vals, width, label=label, color=color)
        ax.axhline(0, color="#7B8790", linewidth=0.8)
        ax.set_title(title, fontsize=11, fontweight="bold", color="#17324D")
        ax.set_xticks(x, target_labels)
        ax.grid(axis="y", color="#D6E0E5", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.tick_params(axis="both", labelsize=8, length=0)
    axes[0].set_ylabel("Diferenca de pontuacao", fontsize=9)
    axes[1].legend(loc="lower center", bbox_to_anchor=(-0.05, -0.31), ncol=3, frameon=False, fontsize=8)
    fig.tight_layout(rect=(0, 0.10, 1, 1))
    chart_gap = CHART_DIR / "train_validation_gaps.png"
    fig.savefig(chart_gap, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    fig, axes = plt.subplots(1, 3, figsize=(11.2, 3.8), sharey=True)
    for ax, (target, target_label) in zip(axes, zip(target_order, target_labels)):
        data = [sessions[(sessions.model == model) & (sessions.target == target)].mcc.dropna().to_numpy() for model in model_order]
        boxes = ax.boxplot(data, patch_artist=True, widths=0.58, showfliers=False)
        for box, color in zip(boxes["boxes"], palette):
            box.set_facecolor(color)
            box.set_alpha(0.8)
        for median in boxes["medians"]:
            median.set_color("white")
            median.set_linewidth(1.6)
        ax.axhline(0, color="#A2ADB5", linewidth=0.7, linestyle="--")
        ax.set_title(target_label, fontsize=11, fontweight="bold", color="#17324D")
        ax.set_xticks([1, 2, 3], ["HGB", "MLP ind.", "MLP comp."], rotation=15, fontsize=8)
        ax.grid(axis="y", color="#D6E0E5", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.tick_params(axis="y", labelsize=8, length=0)
    axes[0].set_ylabel("MCC diario - 25 pregones", fontsize=9)
    fig.suptitle("Variacao do desempenho por pregao no teste", fontsize=12, fontweight="bold", color="#17324D", y=1.02)
    fig.tight_layout()
    chart_daily = CHART_DIR / "daily_mcc_distribution.png"
    fig.savefig(chart_daily, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return chart_mcc_auc, chart_gap, chart_daily


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="CoverKicker", fontName="Arial-Bold", fontSize=9, leading=13, textColor=TEAL, spaceAfter=12))
    styles.add(ParagraphStyle(name="CoverTitle", fontName="Arial-Bold", fontSize=27, leading=32, textColor=NAVY, spaceAfter=12))
    styles.add(ParagraphStyle(name="CoverSubtitle", fontName="Arial", fontSize=13, leading=19, textColor=MID, spaceAfter=16))
    styles.add(ParagraphStyle(name="H1x", fontName="Arial-Bold", fontSize=18, leading=22, textColor=NAVY, spaceBefore=8, spaceAfter=11, keepWithNext=True))
    styles.add(ParagraphStyle(name="H2x", fontName="Arial-Bold", fontSize=12, leading=15, textColor=TEAL, spaceBefore=9, spaceAfter=5, keepWithNext=True))
    styles.add(ParagraphStyle(name="Bodyx", fontName="Arial", fontSize=9.2, leading=13.4, textColor=INK, spaceAfter=7))
    styles.add(ParagraphStyle(name="Smallx", fontName="Arial", fontSize=7.7, leading=10.2, textColor=INK, spaceAfter=4))
    styles.add(ParagraphStyle(name="Captionx", fontName="Arial-Italic", fontSize=7.7, leading=10, textColor=MID, spaceBefore=4, spaceAfter=9))
    styles.add(ParagraphStyle(name="Calloutx", fontName="Arial-Bold", fontSize=10, leading=14, textColor=NAVY, backColor=PALE, borderColor=TEAL, borderWidth=0.7, borderPadding=9, spaceBefore=5, spaceAfter=10))
    styles.add(ParagraphStyle(name="TableHeadx", fontName="Arial-Bold", fontSize=7.4, leading=9, textColor=colors.white, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name="TableCellx", fontName="Arial", fontSize=7.3, leading=9.2, textColor=INK))
    styles.add(ParagraphStyle(name="TableCellSmallx", fontName="Arial", fontSize=6.5, leading=8.2, textColor=INK))
    styles.add(ParagraphStyle(name="Centerx", fontName="Arial", fontSize=8.8, leading=12, textColor=MID, alignment=TA_CENTER))
    return styles


def para(text, style):
    return Paragraph(text, style)


def make_table(rows, widths, styles, small=False, font=7.3):
    head_style = styles["TableHeadx"]
    cell_style = styles["TableCellSmallx"] if small else styles["TableCellx"]
    data = []
    for r_idx, row in enumerate(rows):
        sty = head_style if r_idx == 0 else cell_style
        data.append([x if isinstance(x, Paragraph) else Paragraph(str(x), sty) for x in row])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE]),
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ALIGN", (2, 1), (-1, -1), "CENTER"),
    ]))
    return t


def page_chrome(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(GRID)
        canvas.setLineWidth(0.6)
        canvas.line(17 * mm, A4[1] - 14 * mm, A4[0] - 17 * mm, A4[1] - 14 * mm)
        canvas.setFont("Arial-Bold", 7.5)
        canvas.setFillColor(NAVY)
        canvas.drawString(17 * mm, A4[1] - 11 * mm, "RELATORIO TECNICO | ESTUDO B0 MULTI-ESCALA")
    canvas.setStrokeColor(GRID)
    canvas.line(17 * mm, 13 * mm, A4[0] - 17 * mm, 13 * mm)
    canvas.setFont("Arial", 7.4)
    canvas.setFillColor(MID)
    canvas.drawString(17 * mm, 9 * mm, "Uso interno - resultados de rotulos retrospectivos B0")
    canvas.drawRightString(A4[0] - 17 * mm, 9 * mm, f"{doc.page}")
    canvas.restoreState()


def build_report():
    setup_fonts()
    test, trainval, sessions, all_metrics, cv, contracts = load_data()
    chart_main, chart_gap, chart_daily = make_charts(test, trainval, sessions)
    styles = build_styles()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUT), pagesize=A4,
        leftMargin=17 * mm, rightMargin=17 * mm,
        topMargin=20 * mm, bottomMargin=19 * mm,
        title="Relatorio tecnico - rotulos intradiarios B0",
        author="Estudo interno BovDB",
        subject="Metodologia e resultados da avaliacao de modelos em WIN e IND",
    )
    story = []
    W = A4[0] - 34 * mm

    # Capa e resumo executivo.
    story += [Spacer(1, 20 * mm), para("RELATORIO TECNICO | ESTUDO QUANTITATIVO", styles["CoverKicker"]),
              para("Modelos multi-escala para rotulos intradiarios B0", styles["CoverTitle"]),
              para("Avaliação de rótulos de tendência de 5, 10 e 15 minutos em candles de um minuto", styles["CoverSubtitle"]),
              Spacer(1, 4 * mm),
              para("WIN e IND | Dados de 2 de janeiro a 30 de junho de 2026 | Versão de 26 de outubro de 2026", styles["Bodyx"]),
              para("STATUS: relatório interno de pesquisa. Os bancos de origem e as predições linha a linha não estão autorizados para divulgação pública.", styles["Calloutx"]),
              Spacer(1, 4 * mm), para("Resumo executivo", styles["H1x"]),
              para("Este estudo mede se indicadores causais calculados até o fechamento de cada candle reproduzem os rótulos retrospectivos B0 associados ao mesmo instante. A avaliação não interpreta B0 como verdade independente, não estima direção real de mercado e não mede rentabilidade.", styles["Bodyx"])]
    summary_rows = [
        ["Pergunta", "Resultado principal"],
        ["Modelo compartilhado vs. modelos separados", "Sem vantagem clara. Os intervalos pareados de MCC incluem zero nas três escalas."],
        ["Melhor MCC agregado", "MLP independente em 5 min (0,4925); HistGradientBoosting em 10 min (0,4513) e 15 min (0,4448)."],
        ["Generalização", "A validação cronológica foi mantida no teste posterior; não se observou colapso de desempenho."],
        ["Uso dos resultados", "Reprodução de rótulos B0 retrospectivos. Não há alegação de lucro, execução ou estado verdadeiro do mercado."],
    ]
    story += [make_table(summary_rows, [46 * mm, W - 46 * mm], styles), Spacer(1, 5 * mm),
              para("Escopo da leitura", styles["H2x"]),
              para("O relatório resume as fases de auditoria, protocolo, modelagem, avaliação final e diagnóstico de sobreajuste. As métricas finais foram calculadas a partir da única execução congelada e das predições armazenadas; o diagnóstico de treino foi feito em separado usando somente as partições de treino e validação.", styles["Bodyx"]), PageBreak()]

    # 1 Introdução e dados.
    story += [para("1. Introdução", styles["H1x"]),
              para("Rótulos de tendência podem ser criados por regras de segmentação que usam candles posteriores ao instante rotulado. Um modelo treinado para reproduzir esses rótulos responde a uma pergunta específica: quanto dos rótulos B0 pode ser recuperado a partir de indicadores de mercado disponíveis até o fechamento do candle? Essa pergunta não equivale a prever retorno futuro ou identificar uma tendência verdadeira em tempo real.", styles["Bodyx"]),
              para("O objetivo principal foi comparar três modelos independentes, um para cada escala B0, com um modelo multitarefa que compartilha uma representação e produz três saídas. A hipótese operacional era que as escalas compartilham informação suficiente para que o modelo conjunto melhore ou preserve a reprodução dos rótulos.", styles["Bodyx"]),
              para("2. Dados e população", styles["H1x"]),
              para("Foram usados os bancos internos BovDB de candles e de rótulos B4, sem modificar as fontes. O universo confirmatório é WIN e IND, selecionado por quantidade negociada, negócios e cobertura de sessões observados na fotografia local. Cada contrato permanece como uma série separada; não há costura de vencimentos.", styles["Bodyx"])]
    data_rows = [
        ["Item", "Definição"],
        ["Janela observada", "119 pregões entre 2026-01-02 e 2026-06-30."],
        ["Raízes", "WIN e IND; WDO, WSP e ISP não têm candles intradiários e rótulos B4 nesta base local."],
        ["Divisão temporal", "71 pregões para treino; 23 para validação; 25 para teste final, sem embaralhar datas."],
        ["Teste final", "2026-05-26 a 2026-06-30; 20.488 linhas com features completas; 20.332 na interseção dos três rótulos."],
        ["Dados compartilháveis", "Não autorizados para distribuição pública no momento; hashes e metadados são mantidos nos relatórios do projeto."],
    ]
    story += [make_table(data_rows, [42 * mm, W - 42 * mm], styles),
              para("As raízes menos líquidas ou com poucas sessões foram mantidas fora da análise confirmatória. Essa escolha restringe as conclusões à população acima e não implica que o modelo generalize para outros contratos.", styles["Smallx"]), PageBreak()]

    # 3 Metodologia.
    story += [para("3. Metodologia", styles["H1x"]),
              para("3.1 Alvo e instante de decisão", styles["H2x"]),
              para("Cada feature é alinhada ao rótulo B0 pela mesma chave (ticker, data, hora). A decisão é considerada após o fechamento do candle de um minuto. Não foi aplicado deslocamento para o dia seguinte. Os rótulos B0 são retrospectivos e podem depender de candles posteriores dentro da sessão; portanto, o alvo é a classe B0 anexada ex post ao instante, e não uma classe observável naquele instante.", styles["Bodyx"]),
              para("3.2 Indicadores", styles["H2x"]),
              para("As 11 entradas são retornos logarítmicos de 1, 5 e 15 candles observados consecutivos; corpo e amplitude relativos ao fechamento; volatilidade populacional de retornos em janelas de 5, 15 e 30 linhas; e log1p de volume, negócios e quantidade negociada. Janelas são reiniciadas em gaps, contratos e pregões. Não se criam candles sintéticos nem se usa forward-fill. Campos B4, SIDEWAYS e endpoints de segmentos são excluídos das entradas.", styles["Bodyx"]),
              para("3.3 Modelos", styles["H2x"])]
    model_rows = [
        ["Família", "Configuração resumida"],
        ["Referências simples", "Classe majoritária e regra causal de momentum baseada no retorno de 5 minutos."],
        ["Modelos clássicos", "Regressão logística padronizada e HistGradientBoosting com 50 iterações e até 15 folhas."],
        ["MLP independente", "Uma rede binária por escala; camadas 32 e 16; dropout 0,10; 5 épocas; batch 256."],
        ["MLP compartilhado", "Encoder compartilhado, três cabeças B0 e perda mascarada para alvos ausentes."],
        ["Alvos derivados", "MLP para voto majoritário e regressão de mean_score, comparada à média do treino."],
    ]
    story += [make_table(model_rows, [43 * mm, W - 43 * mm], styles),
              para("3.4 Avaliação e métricas", styles["H2x"]),
              para("A seleção de features, escalonamento e treino respeitam a ordem temporal. Foram usados quatro folds expanding de desenvolvimento; o teste final teve 25 pregões e foi aberto uma vez sob configuração congelada. A comparação principal usa MCC pareado entre MLP independente e compartilhado na amostra comum de três rótulos. Intervalos de 95% usam bootstrap circular em blocos de cinco pregões, com 10.000 replicações; não foram reportados valores-p no teste.", styles["Bodyx"]),
              para("As métricas incluem MCC, acurácia, acurácia balanceada, precisão, recall e F1 por classe, especificidade, ROC-AUC, PR-AUC por average precision, Cohen kappa, Brier, log-loss, ECE de 10 faixas e as quatro células da matriz de confusão. MAE e MSE são usados para mean_score. Métricas adicionais foram calculadas a partir das predições salvas, sem retreino ou seleção baseada no teste.", styles["Bodyx"]), PageBreak()]

    # 4 Resultados quantitativos.
    story += [para("4. Resultados", styles["H1x"]),
              para("4.1 Comparação principal", styles["H2x"]),
              para("A diferença de MCC entre os modelos independentes e compartilhados foi pequena. Os três intervalos incluem zero, o que não sustenta uma vantagem clara da arquitetura compartilhada no teste.", styles["Bodyx"])]
    pairs = [
        ["Alvo", "n comum", "MCC ind.", "MCC comp.", "Diferença", "IC 95% por blocos"],
        ["5 min", "20.332", "0,4934", "0,4882", "+0,0052", "[-0,0002; 0,0102]"],
        ["10 min", "20.332", "0,4436", "0,4403", "+0,0033", "[-0,0057; 0,0121]"],
        ["15 min", "20.332", "0,4306", "0,4306", "-0,00006", "[-0,0052; 0,0051]"],
    ]
    story += [make_table(pairs, [24 * mm, 24 * mm, 25 * mm, 25 * mm, 23 * mm, W - 121 * mm], styles),
              para("O contraste pareado usa somente as 20.332 linhas com os três rótulos presentes. A tabela seguinte usa todas as linhas válidas para cada alvo separadamente, por isso seus n e MCC podem diferir ligeiramente.", styles["Smallx"]),
              Spacer(1, 3 * mm), Image(str(chart_main), width=W, height=87 * mm),
              para("Figura 1. MCC e ROC-AUC agregados no teste para os três modelos centrais. As métricas descrevem reprodução de B0, não previsão de retorno ou desempenho econômico.", styles["Captionx"]),
              para("4.2 Métricas por escala", styles["H2x"])]
    results_rows = [["Modelo", "Alvo", "n", "MCC", "Acuracia", "Precisao +", "Recall +", "ROC-AUC", "PR-AUC"]]
    model_labels = {"hist_gradient_boosting": "HistGradientBoosting", "independent_mlp": "MLP independente", "shared_multitask_mlp": "MLP compartilhado"}
    for target, tlabel in zip(["trend_5m", "trend_10m", "trend_15m"], ["5 min", "10 min", "15 min"]):
        for model in ["hist_gradient_boosting", "independent_mlp", "shared_multitask_mlp"]:
            r = test.loc[(model, target)]
            results_rows.append([model_labels[model], tlabel, f"{int(r.n):,}".replace(",", "."), f"{r.mcc:.4f}", f"{r.accuracy:.4f}", f"{r.precision_1:.4f}", f"{r.recall_1:.4f}", f"{r.roc_auc:.4f}", f"{r.pr_average_precision:.4f}"])
    story += [make_table(results_rows, [37 * mm, 15 * mm, 13 * mm, 15 * mm, 17 * mm, 19 * mm, 17 * mm, 18 * mm, W - 151 * mm], styles, small=True),
              para("A maior MCC foi 0,4925 do MLP independente em 5 min; HistGradientBoosting obteve as maiores MCCs agregadas em 10 min (0,4513) e 15 min (0,4448). ROC-AUC e PR-AUC avaliam a ordenação dos escores em relação aos rótulos B0; não devem ser lidas como probabilidade de movimento verdadeiro.", styles["Smallx"]), PageBreak()]

    # 5 Matrizes, resultados derivados.
    story += [para("5. Detalhamento dos resultados", styles["H1x"]),
              para("5.1 Matrizes de confusão", styles["H2x"]),
              para("As contagens abaixo usam a decisão fixa de 0,5: TN = verdadeiro negativo; FP = falso positivo; FN = falso negativo; TP = verdadeiro positivo.", styles["Bodyx"])]
    confusion_rows = [["Alvo", "Modelo", "TN", "FP", "FN", "TP"]]
    for target, tlabel in zip(["trend_5m", "trend_10m", "trend_15m"], ["5 min", "10 min", "15 min"]):
        for model in ["hist_gradient_boosting", "independent_mlp", "shared_multitask_mlp"]:
            r = test.loc[(model, target)]
            confusion_rows.append([tlabel, model_labels[model], f"{int(r.confusion_00):,}".replace(",", "."), f"{int(r.confusion_01):,}".replace(",", "."), f"{int(r.confusion_10):,}".replace(",", "."), f"{int(r.confusion_11):,}".replace(",", ".")])
    story += [make_table(confusion_rows, [26 * mm, 54 * mm, 24 * mm, 24 * mm, 24 * mm, W - 152 * mm], styles),
              para("5.2 Alvo de maioria e score suave", styles["H2x"]),
              para("Para o alvo de maioria, o MLP obteve MCC 0,4624 e acurácia 0,7302. Para mean_score, o MLP reduziu o MAE de 0,4119 para 0,2837 e o MSE de 0,1918 para 0,1210 em relação à média constante do treino. mean_score é a fração determinística dos votos B0; a redução de erro não confirma uma probabilidade verdadeira.", styles["Bodyx"]),
              para("5.3 Robustez entre blocos, raízes e contratos", styles["H2x"]),
              para("Os resultados de WIN e IND são próximos nos agregados. MCC de 5 min e 10 min permaneceu relativamente estável entre os três blocos de teste. O MCC de 15 min aumentou no terceiro bloco para os modelos avaliados, padrão descritivo que pode refletir variação temporal. WINV26 teve somente 149 observações no teste; seus resultados por contrato são instáveis e não devem sustentar conclusões isoladas.", styles["Bodyx"]),
              para("As tabelas completas por raiz, bloco e contrato permanecem nos CSVs do projeto. A unidade de incerteza da análise principal são os pregões e blocos temporais, não cada candle como se fosse uma observação independente.", styles["Bodyx"]), PageBreak()]

    # 6 Diagnóstico de overfitting.
    story += [para("6. Diagnóstico de sobreajuste e estabilidade", styles["H1x"]),
              para("Uma reprodução diagnóstica em CPU usou os mesmos parâmetros e seeds congelados e ajustou modelos apenas na partição de treino. O teste não foi carregado durante esse ajuste. O gap aparente compara o desempenho in-sample no treino com a validação cronológica; como esperado, treino é otimista e essa diferença é um sinal de alerta, não uma estimativa imparcial de erro futuro.", styles["Bodyx"]),
              Image(str(chart_gap), width=W, height=83 * mm),
              para("Figura 2. Gap de MCC e Brier entre treino e validação. Todos os modelos têm gap positivo; o tamanho é moderado, com o maior MCC em 15 min.", styles["Captionx"])]
    gap_rows = [["Modelo", "MCC gap, 5m", "MCC gap, 10m", "MCC gap, 15m", "Faixa" ]]
    tv = trainval.set_index(["model", "target"])
    for model in ["hist_gradient_boosting", "independent_mlp", "shared_multitask_mlp", "logistic_regression"]:
        vals = [tv.loc[(model, t), "mcc_gap_train_minus_validation"] for t in ["trend_5m", "trend_10m", "trend_15m"]]
        gap_rows.append([model_labels.get(model, "Regressao logistica"), *[f"{v:.3f}" for v in vals], f"{min(vals):.3f} a {max(vals):.3f}"])
    story += [make_table(gap_rows, [47 * mm, 26 * mm, 27 * mm, 27 * mm, W - 127 * mm], styles),
              para("Nos nove pares MLP-alvo, o gap de MCC foi 0,022 a 0,035. HistGradientBoosting ficou em 0,026 a 0,041. Apesar do gap, as métricas de teste não caíram em relação à validação congelada: as nove diferenças de MCC foram não negativas, entre +0,001 e +0,012.", styles["Bodyx"]), PageBreak(),
              para("6.1 Dispersão entre pregões de teste", styles["H2x"]),
              Image(str(chart_daily), width=W, height=82 * mm),
              para("Figura 3. Distribuição do MCC por pregão nos 25 pregões de teste. Nenhum pregão apresentou MCC diário negativo para os três modelos centrais. Os pregões são temporalmente dependentes.", styles["Captionx"])]
    daily_rows = [["Modelo", "Alvo", "MCC medio", "DP", "P10-P90", "Pregoes negativos"]]
    for model in ["hist_gradient_boosting", "independent_mlp", "shared_multitask_mlp"]:
        for target, tlabel in zip(["trend_5m", "trend_10m", "trend_15m"], ["5 min", "10 min", "15 min"]):
            g = sessions[(sessions.model == model) & (sessions.target == target)].mcc.dropna()
            daily_rows.append([model_labels[model], tlabel, f"{g.mean():.3f}", f"{g.std(ddof=1):.3f}", f"{g.quantile(.1):.3f} a {g.quantile(.9):.3f}", str(int((g < 0).sum()))])
    story += [make_table(daily_rows, [43 * mm, 18 * mm, 22 * mm, 15 * mm, 28 * mm, W - 126 * mm], styles, small=True),
              para("Os quatro folds expanding de desenvolvimento tiveram MCC médio e desvio-padrão de 0,487 +/- 0,012 em 5 min, 0,447 +/- 0,031 em 10 min e 0,442 +/- 0,024 em 15 min. Os folds compartilham períodos de treino; os desvios são descritivos, não intervalos independentes.", styles["Bodyx"]), PageBreak()]

    # 7 Interpretação e conclusão.
    story += [para("7. Interpretação e limites", styles["H1x"]),
              para("A evidência indica algum ajuste aos dados de treino, visível no gap de 0,02 a 0,04 MCC. No entanto, não há sinal de colapso no período de teste: a validação foi mantida e as métricas de teste foram ligeiramente superiores. A conclusão apropriada é que existe possibilidade de sobreajuste moderado, sem evidência de sobreajuste severo nesta amostra. Uma única janela de 25 pregões não permite descartar o risco em outros regimes.", styles["Bodyx"]),
              para("A auditoria de vazamento registrou divisão cronológica por data, folds ordenados, escalonamento restrito ao treino e reinício de estado de features em gaps, contratos e pregões. Isso reduz risco de vazamento de implementação. Porém, a natureza retrospectiva do alvo continua sendo uma limitação conceitual do estudo.", styles["Bodyx"]),
              para("Limitações que definem o alcance dos resultados", styles["H2x"])]
    limitations = [
        "B0 é retrospectivo e não tem validação independente como estado verdadeiro de mercado.",
        "A janela cobre seis meses e duas raízes confirmatórias; extrapolação para outros períodos e instrumentos não foi testada.",
        "O teste tem 25 pregões; sua incerteza temporal é material mesmo com mais de 20 mil candles.",
        "Não foram estudados retorno futuro executável, custos, slippage, latência ou uma estratégia de negociação.",
        "Os dados e predições são internos; a publicação depende de autorização do titular e de um plano reproduzível de acesso.",
    ]
    for item in limitations:
        story.append(Paragraph("&#8226; " + item, styles["Bodyx"]))
    story += [para("8. Conclusão", styles["H1x"]),
              para("Nos dados locais WIN/IND, o modelo compartilhado não superou claramente os modelos independentes na reprodução dos rótulos B0 em 5, 10 e 15 minutos. HistGradientBoosting teve o maior MCC agregado em 10 e 15 minutos; o MLP independente ficou ligeiramente à frente em 5 minutos. Há um gap aparente treino-validação moderado, mas não se observou degradação do teste final frente à validação.", styles["Bodyx"]),
              para("Estes resultados descrevem previsão de rótulos B0 retrospectivos. Não demonstram previsão da direção real do mercado nem rentabilidade.", styles["Calloutx"]),
              para("Próxima evidência necessária", styles["H2x"]),
              para("Para sustentar generalização, será necessária uma janela posterior e intocada, mais anos e instrumentos, e uma hipótese de previsão que defina claramente o evento futuro. Se o objetivo for falar de mercado real ou lucro, será necessária uma referência independente e avaliação com custos de execução. O teste atual já foi aberto e deve permanecer fora de qualquer seleção ou ajuste.", styles["Bodyx"]),
              para("Documentos e dados de suporte", styles["H2x"]),
              para("O relatório foi composto a partir do manuscrito interno, protocolo congelado e relatórios de avaliação final, métricas suplementares, auditoria de vazamento e diagnóstico de sobreajuste. Os bancos SQLite e arquivos linha a linha não estão incorporados neste PDF.", styles["Smallx"]),
              Spacer(1, 2 * mm),
              para("Documento interno | NCA Optimizer Benchmark | 26 de outubro de 2026", styles["Centerx"])]

    doc.build(story, onFirstPage=page_chrome, onLaterPages=page_chrome)
    print(OUT)


if __name__ == "__main__":
    build_report()
