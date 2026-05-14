"""
Extrait toutes les figures embarquées du notebook analysis.ipynb
et les sauvegarde dans outputs/figures/ en PNG.
"""

import json
import base64
from pathlib import Path

# Chemins
notebook_path = Path("notebooks/analysis.ipynb")
output_dir = Path("outputs/figures")
output_dir.mkdir(parents=True, exist_ok=True)

# Charger le notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Parcourir toutes les cellules et extraire les images
figure_count = 0
for cell_idx, cell in enumerate(nb.get("cells", [])):
    if cell.get("cell_type") != "code":
        continue
    
    for output in cell.get("outputs", []):
        # Cas 1: image/png dans display_data ou execute_result
        data = output.get("data", {})
        if "image/png" in data:
            figure_count += 1
            image_b64 = data["image/png"]
            # Parfois c'est une liste de strings (multi-line)
            if isinstance(image_b64, list):
                image_b64 = "".join(image_b64)
            image_bytes = base64.b64decode(image_b64)
            output_file = output_dir / f"fig_{figure_count:02d}_cell{cell_idx}.png"
            with open(output_file, "wb") as f:
                f.write(image_bytes)
            print(f"Saved: {output_file}")

print(f"\n✅ Total figures extracted: {figure_count}")
print(f"📁 Output directory: {output_dir.resolve()}")