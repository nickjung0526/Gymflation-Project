## Gymflation Project Overview
  The "Gymflation" project is an automated Data Engineering and Financial Analysis pipeline designed to extract, clean, and visualize macro-economic trends across the public fitness industry. By utilizing **SEC EDGAR API**, this project tracks the quarterly financial performance of 11 major publicly traded companies, grouped into four core categories: Apparel, Gyms, Consumables & Supplements, and Wearables & Equipment

  The goal of this analysis is to cut through noise of quartlerly reports and identify true year-over-year growth trends in consumer spending.
  

## Tech Stack
- **Language:** Python
- **Data Extraction**: SEC EDGAR REST API (JSON parsing)
- **Data Manipulation & Cleaning:** Pandas, NumPy
- **Visualization:** Plotly (Interactive Time-Series Dashboards

## Data Engineering Pipeline
  Raw SEC financial data is notoriously volatile and difficult to standardize across different models. This pipeline executes several critical transformation steps to prepare the data for analysis:
  1) **Dynamic CIK Mapping**: Automates the extraction of raw **XBRL** financial data (Net Revenue, Cost of Revenu, Operating Income) for tickers inlcuding `LULU`, `PLANT`, `CELH`, `GRMN`, and others.
  2) **Standardization of Service Sector Metrics**: Implemented custom filtering logic (`Net_Revenue != 0.0`) to properly handle service-based entities that report standard operating expenses rather than traditional physical "Cost of Goods Sold" metrics.
  3) **Macro-Categorization**: Mapped individual company tickers into aggregated industry buckets to evaluate sector-wide health rather than single-stock performance
  4) **Volatility Smoothing**: Applied a 4-quarter rolling average to all Year-over-Year (YoY) growth calculations, effectively mitigating the violent seasonal spikes inherent in raw quarterly retail data to reveal true underlying trends

## Key Analytical Insights
<img width="1088" height="316" alt="image" src="https://github.com/user-attachments/assets/030b893f-b3e3-4060-bd97-37a7aaf2093d" />

#### From 2021 - 2025, the mean average each category saw in YoY:
- **Apparel**: 107.73%
- **Consumables & Supplements**: 123.13%
- **Gyms**: 148.40%
- **Wearables**: 86.06%

#### From 2025-Now, the mean average each category saw in YoY:
- **Apparel**: -10.38%
- **Consumables & Supplements**: -3.23%
- **Gyms**: -43.30%
- **Wearables**: 43.46%
