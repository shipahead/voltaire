# Voltaire 🌱

> 72-hour solar and wind energy forecasting system for the German power grid based on publicly available meteorological data.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

Solar and wind energy are weather-dependent and hard to plan. Grid operators 
and energy traders need precise 24–72h forecasts to manage storage, purchase 
balancing energy, and predict electricity prices.

Voltaire builds exactly this system using real public data from the German 
power grid — combining machine learning with physical domain knowledge 
(sun position, wind height profiles) to produce calibrated forecasts with 
confidence intervals.

**Target performance:**
- MAPE < 8% for solar yield (daily average)
- MAPE < 10% for wind yield (hourly)

---

## Data Sources

| Source | Description | Frequency |
|--------|-------------|-----------|
| [ENTSO-E Transparency Platform](https://transparency.entsoe.eu) | German power generation 2019–2024 | Hourly |
| [DWD Open Data](https://opendata.dwd.de) | Wind, irradiance, temperature (400+ stations) | Hourly |
| [Open-Meteo API](https://open-meteo.com) | 7-day weather forecast | Hourly |

---

## Project Structure
```
voltaire/
├── data/
│   ├── raw/              # Original data — never modified
│   ├── processed/        # Cleaned, model-ready data
│   └── external/         # Third-party data
├── notebooks/            # Numbered Jupyter notebooks
├── src/                  # Python package
│   ├── data.py           # Data loading and processing
│   ├── features.py       # Feature engineering
│   ├── models.py         # Training and prediction
│   └── visualize.py      # Plotting functions
├── app/                  # Deployment (FastAPI + Streamlit)
├── models/               # Saved trained models
├── reports/figures/      # Exported charts
├── tests/                # Unit and integration tests
├── config.py             # Paths, constants, hyperparameters
└── environment.yml       # Conda environment
```

---

## Setup

**Requirements:** Miniconda installed on your machine.
```bash
# Clone the repo
git clone https://github.com/shipahead/voltaire.git
cd voltaire

# Create and activate the conda environment
conda env create -f environment.yml
conda activate env_voltaire
```

---

## Results

*Model training in progress — results will be updated here.*

---

## Roadmap

- [x] Project structure and dev environment
- [x] EnergyDataLoader class
- [ ] ENTSO-E data ingestion
- [ ] DWD weather data integration
- [ ] Exploratory data analysis
- [ ] Feature engineering (lag, Fourier, sun position)
- [ ] XGBoost + Random Forest models
- [ ] Walk-forward backtesting
- [ ] FastAPI deployment
- [ ] Live dashboard

---

## License

MIT License — see [LICENSE](LICENSE) for details.