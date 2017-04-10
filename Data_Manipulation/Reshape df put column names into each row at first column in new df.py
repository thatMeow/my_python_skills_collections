df1.columns = df1.columns.str.split("_", expand=True)
df1.stack(level=0).rename_axis((None, "item")).reset_index("item")

# http://stackoverflow.com/questions/43210838/python-restructure-dataframe-move-column-names-to-rows-reshape-dataframe
