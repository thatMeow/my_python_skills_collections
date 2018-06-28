df['decile'] = pd.qcut(df['score'], 10, labels=np.arange(10, 0, -1))

# get score cutoffs
df = f1.groupby(['decile']).agg({'freedom_gate_predict_score' : [np.min, np.max]})
df.columns = ['_'.join(col).strip() for col in df.columns.values]
