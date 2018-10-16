# pandas02.py
import pandas as pd

input_file = './day14/sales_2017.xlsx'
output_file = './day14/output/pandas_output.xls'

df = pd.read_excel(input_file, sheetname='january_2017')
new_df = df[df['Sale Amount'].astype(float) > 1400.0]

writer = pd.ExcelWriter(output_file)
new_df.to_excel(writer, sheet_name='jan_17_output', index=False)
writer.save()
print("Done.")