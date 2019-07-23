# convert a column in a DataFrame to dummies variables and delete the column

def convert_to_dummies(df, column):

    dummies = pd.get_dummies(df[column]).rename(columns=lambda x: column + '_' + str(x))
    return pd.concat([df, dummies], axis=1).drop(column, axis=1)
