## Gymflation Project (WIP)
I'm personally interested how gym and social media correlate, particularly in how much revenue gym oriented companies have amassed since the rise of social media influence. 
How much did they make since it surged online? How popular has it gotten? I want to know!

## How It's Made
**Tech used**: Python, pandas, camelot, CSV, Git/Github
This project is currently built as a Python-based financial data extraction pipeline. I started by collecting Annual Report PDFs from public fitness and athletic apparel companies, then used Camelot to extract financial tables from specific pages of each report. Rather than scraping the entire PDF, I manually identified the pages containing the results of operations to reduce noice from unrelated tables. 

For the first version, I focused on Under Armour's annual report and extracted key financial metrics such as: 
- net revenues
- gross profits
- selling/general/administrative expensives
- income from operations
- net income

 After Camelot extracted the table, I used pandas to filter only relevant financial rows, clean accounting-style values such as parantheses for losses, and reshpae the data from a report-style table into a usable analysis-ready format.



Milestone 1: Extracted Under Armour financial metrics from PDF
