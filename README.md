## Gymflation Project (WIP)
I'm personally interested in how gym culture and social media correlate, particularly in how much revenue fitness-oriented companies have amassed since the rise of fitness influencers. How much did these companies make since gym culture surged online? How popular has it actually gotten? This project aims to find out by correlating financial data with Google Trends search volume.

## Tech Stack
**Tech used**: Python, Pandas, Jupyter Notebook, SEC EDGAR API, Requests, Git/GitHub

## The Evolution of the Project

### Phase 1: The PDF Scraping Bottleneck
This project initially started by collecting Annual Report (10-K) PDFs from public fitness and athletic apparel companies. I used Camelot to extract financial tables from specific pages to reduce noise. 

For the first version, I focused on Under Armour's annual report, extracting key metrics like `net revenues`, `gross profit`, and `operating income`. After Camelot extracted the table, I used Pandas to clean accounting-style values (like parentheses for losses) and reshape the data.

### Phase 2: The Pivot to the SEC EDGAR API (Current Architecture)
I quickly realized two major limitations with the PDF approach:
1. **Formatting Inconsistencies:** Scraping tables out of 10-K PDFs for multiple different companies across multiple years is an absolute nightmare of formatting inconsistencies.
2. **Sample Size:** Annual reports only provide one data point per year, which is entirely too small of a sample size to prove any meaningful correlation against highly granular Google Trends data. 

To fix this, I completely rebuilt the extraction pipeline to directly query the **SEC EDGAR API** (`companyfacts` endpoint). 

### How It Works Now
The current Python/Pandas pipeline automatically extracts **Quarterly (10-Q)** financial data for multiple companies at once. Features of the pipeline include:
* **Dynamic CIK Mapping:** Maps company tickers (like LULU or UAA) to their zero-padded 10-digit SEC Central Index Keys.
* **Dictionary Fallback System:** SEC XBRL accounting tags are inconsistent (e.g., Under Armour uses `Revenues`, while Lululemon uses `SalesRevenueNet`). The script uses a fallback dictionary to dynamically hunt down the correct tags without crashing.
* TO DO: **Segment Data Filtering:** The script automatically detects and removes nested segment data (e.g., isolating total Deckers revenue from specific HOKA or UGG segments) to prevent double-counting.
* **Automated Data Cleaning:** Filters exclusively for 10-Q reports, cleans the indexing, and builds a master DataFrame tagged by Ticker, Date, Metric, and Value.

## Current Milestones
- [x] Milestone 1: Built master SEC API pipeline to fetch and clean quarterly (10-Q) top-line financial data for target companies.
- [x] Milestone 2: Implemented dictionary fallback system for inconsistent XBRL tags and filtered out duplicate segment data.
- [ ] Milestone 3: Transform long-format data to wide-format and calculate key efficiency margins (Gross Margin %, Operating Margin %).
- [ ] Milestone 4: Import Google Trends data and plot correlations against quarterly revenues.
