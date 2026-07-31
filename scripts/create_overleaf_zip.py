import os
import zipfile

def create_overleaf_zip():
    base_dir = os.path.join('article', 'manuscript')
    zip_filename = os.path.join('article', 'nca_manuscript_overleaf_template.zip')
    
    files_to_pack = [
        'main.tex',
        'titlepage.tex',
        'references.bib',
        'sn-jnl.cls',
        'sn-mathphys-num.bst',
        'sn-mathphys.bst',
        os.path.join('sections', 'introduction.tex'),
        os.path.join('sections', 'related_work.tex'),
        os.path.join('sections', 'data.tex'),
        os.path.join('sections', 'methodology.tex'),
        os.path.join('sections', 'results.tex'),
        os.path.join('sections', 'discussion.tex'),
        os.path.join('sections', 'conclusion.tex'),
        os.path.join('sections', 'declarations.tex'),
        os.path.join('figures', 'temporal_split.pdf'),
        os.path.join('figures', 'methodology_overview.pdf'),
        os.path.join('figures', 'convergence_curves.pdf'),
        os.path.join('figures', 'metrics_boxplots.pdf'),
        os.path.join('figures', 'financial_equity_curves.pdf'),
    ]

    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for rel_path in files_to_pack:
            abs_path = os.path.join(base_dir, rel_path)
            if os.path.exists(abs_path):
                zipf.write(abs_path, arcname=rel_path)
                print(f"Packed: {rel_path}")
            else:
                print(f"WARNING: File not found: {abs_path}")

    print(f"\nZIP file successfully created at: {zip_filename}")
    print(f"Size: {os.path.getsize(zip_filename) / 1024:.2f} KB")

if __name__ == '__main__':
    create_overleaf_zip()
