# Oil Shocks & Global Equity Markets

> Empirical study of oil price transmission to developed and emerging equity markets — Regime-dependent OLS + VAR + IRF (1990–2026).

**🌐 [Read the full website →](https://RioDimitri.github.io/oil-shocks-equity-markets/)**

📄 [Full report (PDF)](report/EMIF_oil_equity_report.pdf) · 📓 [Notebook](notebooks/analysis.html) · 💻 [Analysis code](notebooks/analysis.ipynb)

---

## TL;DR

- **Methods**: Static OLS with asymmetric and state-dependent specifications, Newey-West HAC inference, three VAR systems with Granger causality and orthogonalised IRFs, out-of-sample forecasting.
- **Sample**: ~9,400 daily observations (1990–2026) on Brent crude, MSCI World, MSCI EM, US 10-year yield, plus 434 monthly macro observations (CFNAI, ISM, Industrial Production).
- **Main findings**: Oil-equity transmission is positive but short-lived (~1 day half-life). No robust evidence of amplification in recessions across specifications. No meaningful difference between developed and emerging markets. Out-of-sample forecasts do not outperform the historical mean — consistent with Welch & Goyal (2008).

## Repository structure
.
├── index.qmd, methodology.qmd, results.qmd, notebook.qmd, about.qmd
├── _quarto.yml              # Quarto website config
├── styles.css               # custom styling
├── notebooks/
│   ├── analysis.ipynb       # main Jupyter notebook
│   └── analysis.html        # rendered notebook (embedded in site)
├── outputs/figures/         # all generated figures (PNG)
├── report/
│   └── EMIF_oil_equity_report.pdf
├── extract_figures.py       # script to extract figures from notebook
└── rename_figures.py        # script to rename figures with descriptive labels

## Context

This empirical study was conducted in April 2026 as the first project of the *Empirical Methods in Finance* course of the MSc Finance programme at HEC Lausanne.

## Reproducibility

The analysis is conducted in Python 3 with `pandas`, `numpy`, `statsmodels`, `matplotlib`. To reproduce locally:

```bash
git clone https://github.com/RioDimitri/oil-shocks-equity-markets.git
cd oil-shocks-equity-markets
pip install pandas numpy statsmodels matplotlib jupyter
jupyter notebook notebooks/analysis.ipynb
```

The financial dataset used in the original study was provided via the HEC Bloomberg subscription and is not redistributed here. Equivalent public proxies are available on FRED (Brent, CFNAI, ISM, Industrial Production, US Treasury yields) and via free ETF tickers (URTH for MSCI World, EEM for MSCI EM).

## License

Code released under the [MIT License](LICENSE).

## Contact

- **Email**: prouvostdimitri@gmail.com
- **GitHub**: [@RioDimitri](https://github.com/RioDimitri)