# check out select_col_by_dtype.py for column selection based on dtype

spearman = data[numerical_features + [target]].corr("spearman")
kendall = data[numerical_features + [target]].corr("kendall")
pearson = data[numerical_features + [target]].corr("pearson")

p = pearson[target].rename("Pearson")
k = kendall[target].rename("Kendall")
s = spearman[target].rename("Spearman")

from pandas import DataFrame

corr = DataFrame(data = p)
corr = corr.assign(Spearman = s)
corr = corr.assign(Kendall = k)

from IPython.display import display

display(corr.round(2).sort_values("Pearson", ascending=False))
