# Create a dictionary mapping the column A value to the multiplication value, then use map on column A and multiply it against column B:
# http://stackoverflow.com/questions/44012855/python-multiplication-based-on-row-values/44013267#44013267


x = 10, y = 20, z = 30

df = pd.DataFrame({'A':['a','b','c'],
                   'B':[6,7,8]})

# Here is what I want to do:
# Create a new column 'C':

If df['A'] == 'a', df['C'] = df['B']*x
If df['A'] == 'b', df['C'] = df['B']*y
If df['A'] == 'c', df['C'] = df['B']*z

# Answer:

mul_map = {'a': 10, 'b': 20, 'c': 30}
df['C'] = df['B'] * df['A'].map(mul_map)
