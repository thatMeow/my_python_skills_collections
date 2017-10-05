# http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html


from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
X = pd.DataFrame(df.drop(['Churn?'], axis=1))
robust_scaled_df = scaler.fit_transform(X)
robust_scaled_df = pd.DataFrame(robust_scaled_df, columns=X.columns)

# concat
df = pd.concat([robust_scaled_df, df['Churn?']], axis=1)
df.head()
