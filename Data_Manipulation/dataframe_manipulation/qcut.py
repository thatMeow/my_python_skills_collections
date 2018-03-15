joined['decile'] = pd.qcut(joined['score'], 10, labels=np.arange(10, 0, -1))
