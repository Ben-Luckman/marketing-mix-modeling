# Marketing Mix Modeling

A regression-based Marketing Mix Model that quantifies the incremental impact of seven marketing channels on lead generation, estimates channel-level ROI, and recommends budget reallocations using marginal returns.

## Approach

| Step | Method |
|------|--------|
| Carryover effects | Adstock transformation with grid-searched decay rates |
| Diminishing returns | Hill saturation function |
| Controls | Seasonality (sin/cos), trend, unemployment, competitor spend, holidays |
| Model selection | OLS vs Ridge regression via time-series cross-validation |
| Diagnostics | VIF, residual analysis, Newey-West HAC standard errors |
| Optimization | Marginal ROI from Hill derivative, budget reallocation simulation |

## Dataset

104 weeks of synthetic marketing data across TV, Radio, Paid Search, Paid Social, OOH, OTT, and SEO channels. Generated via `generate_datasets.py`.

## Repository Structure

```
├── marketing_mix_modeling.ipynb   # Full analysis notebook
├── 01_marketing_mix_modeling.csv  # Weekly marketing dataset
├── generate_datasets.py           # Dataset generation script
└── README.md
```

## Requirements

- Python 3.8+
- pandas, numpy, matplotlib, seaborn
- statsmodels
- scikit-learn
- scipy
