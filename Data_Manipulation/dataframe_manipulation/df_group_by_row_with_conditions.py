# http://stackoverflow.com/questions/43987070/python-dataframe-sum-by-row-with-conditions/43987132#43987132

import pandas as pd
df = pd.DataFrame({'a': ['day1','day1','day1','day2','day2','day2'], 'b': ['x','z','y','x','z','y'], 'c':[9,1,6,0,5,6], 'd':[6,9,1,3,5,9]})

df_desired = pd.DataFrame({'a': ['day1','day1','day2','day2'], 'b': ['v','y','v','y'], 'c':[10,6,5,6], 'd':[15,1,8,9]})

# answer
df.replace({'b':{'x':'v','z':'v'}}).groupby(['a','b'], as_index=False).sum()



