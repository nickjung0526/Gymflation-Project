import pandas as pd
import camelot 
import re

pdf_path = "PDFS/UnderArmor-2025-AnnualReport.pdf"

tables = camelot.read_pdf(
    pdf_path, flavor = "stream", pages = "35")

rows_to_keep = {
    "Net revenues": "total_net_revenue",
    "Gross profit": "gross_profit",
    "Selling, general and administrative expenses": "sga_expenses",
    "Income (loss) from operations": "operating_income",
    "Net income (loss)": "net_income"
}

print(f"Number of tables found: {len(tables)}")

# for i, table in enumerate(tables):
#     print(f"\n-- Table {i} ---")
#     print(table.df)
    
ua_df = tables[1].df
print(f"the original table I picked: {ua_df}", "\n")

ua_clean = ua_df[[0, 2, 4]].copy()
ua_clean.columns = ["Metric (thousands)", "2025", "2024"]
# print(ua_clean)

# deleting the row ((In thousands)          2025       2024)
ua_clean = ua_clean.drop([0,1, 2])
# print(ua_clean, "\n")

ua_clean = ua_clean[ua_clean["Metric (thousands)"].isin(rows_to_keep.keys())]
# mapping the messy variable names to assigned in rows_to_keep
ua_clean["Metric (thousands)"] = ua_clean["Metric (thousands)"].map(rows_to_keep)


ua_long_df = ua_clean.melt(id_vars = "Metric (thousands)",
                        var_name = "fiscal_year",
                        value_name = "value")


print(f"This is UA_LONG: {ua_long_df}", "\n")

## After cleaning the commas and $
ua_long_df['value'] = (
    ua_long_df['value']
    .str.replace(r"[\$,]", "", regex = True)
    .str.replace(r"\((.*?)\)", r"-\1", regex = True)
    .astype(int)
)
print(ua_long_df, ua_long_df.dtypes)

# Pivoting the table
out = ua_long_df.pivot_table(
    index = "fiscal_year",
    columns = "Metric (thousands)",
    values = "value",
    aggfunc = "first"
).reset_index()
print(f"This is what I turned it into: {out}")


