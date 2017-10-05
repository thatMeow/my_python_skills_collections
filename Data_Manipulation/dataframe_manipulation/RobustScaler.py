# http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html


from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
X = pd.DataFrame(df.drop(['target'], axis=1))
X = scaler.fit_transform(X)
X = pd.DataFrame(X, columns=X.columns)
X.head()
