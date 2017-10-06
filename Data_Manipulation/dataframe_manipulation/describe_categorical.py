

def describe_categorical(df):

    """
    Just like df.descrile() but this function only returns description for categorical variables
    """
    
    from IPython.display import display, HTML
    display (HTML(df[df.columns[df.dtypes='object']].describe().to_html()))

