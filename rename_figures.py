"""
Renomme les figures clés extraites du notebook avec des noms descriptifs.
Garde aussi les copies originales fig_XX_cellYY.png au cas où.
"""

import shutil
from pathlib import Path

figures_dir = Path("outputs/figures")

# Mapping: ancien nom → nouveau nom
renames = {
    "fig_02_cell16.png":  "descriptives_skewness_kurtosis.png",
    "fig_03_cell23.png":  "descriptives_acf_returns.png",
    "fig_04_cell24.png":  "descriptives_distributions.png",
    "fig_05_cell33.png":  "data_monthly_macro_overview.png",
    "fig_06_cell36.png":  "cross_correlation_matrix.png",
    "fig_07_cell39.png":  "oil_decomposition_pos_neg.png",
    "fig_08_cell40.png":  "equity_conditional_on_oil_direction.png",
    "fig_09_cell57.png":  "ols_baseline_residuals.png",
    "fig_10_cell69.png":  "oil_effect_by_regime_cfnai.png",
    "fig_11_cell71.png":  "monthly_oil_returns_recessions.png",
    "fig_12_cell95.png":  "robustness_interaction_specifications.png",
    "fig_13_cell97.png":  "macro_indicators_robustness.png",
    "fig_14_cell119.png": "irf_var_world_p7.png",
    "fig_15_cell120.png": "irf_var_em_p7.png",
    "fig_16_cell132.png": "irf_macro_var_p2.png",
    "fig_17_cell137.png": "forecast_msci_world.png",
    "fig_18_cell140.png": "forecast_macro_var.png",
    "fig_19_cell160.png": "irf_var_world_p1.png",
    "fig_20_cell161.png": "irf_var_em_p1.png",
}

renamed_count = 0
skipped_count = 0

for old_name, new_name in renames.items():
    src = figures_dir / old_name
    dst = figures_dir / new_name
    
    if not src.exists():
        print(f"⚠️  Source not found, skipping: {old_name}")
        skipped_count += 1
        continue
    
    # Copie au lieu de renommer (garde l'original au cas où)
    shutil.copy(src, dst)
    print(f"✅ {old_name} → {new_name}")
    renamed_count += 1

print(f"\nRenamed: {renamed_count}")
print(f"Skipped: {skipped_count}")
print(f"\n📁 Check the figures in: {figures_dir.resolve()}")