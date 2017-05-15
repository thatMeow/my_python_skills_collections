import pandas as pd
from pandas import DataFrame, Series
from pandas.tseries.offsets import MonthEnd
from openpyxl import load_workbook # this library enables us writing to existing excel file without overwriting


book = load_workbook(control_excel)
writer = pd.ExcelWriter(control_excel, engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
df.to_excel(writer, "volume_finance_input", index=False)
writer.save()
