df['decile'] = pd.qcut(df['score'], 10, labels=np.arange(10, 0, -1))

# get score cutoffs
cutoffs = df.groupby(['decile']).agg({'score' : [np.min, np.max]})
cutoffs.columns = ['_'.join(col).strip() for col in cutoffs.columns.values]
