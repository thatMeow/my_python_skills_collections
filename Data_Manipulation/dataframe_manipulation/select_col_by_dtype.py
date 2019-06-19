data = read_csv("../input/train.csv")

# Features
target = "SalePrice"
features = data.columns.tolist()

features
features_by_dtype = {}

for feature in features:
    
    feature_dtype = str(data.dtypes[feature])
    
    try:
        features_by_dtype[feature_dtype]
    except KeyError:
        features_by_dtype[feature_dtype] = []
        
    
    features_by_dtype[feature_dtype].append(feature)

dtypes = features_by_dtype.keys()


# Categorical Features
categorical_features = features_by_dtype["object"]

# Binary Features
binary_features = [c for c in categorical_features if len(data[c].unique()) == 2]

# Numerical Features
float_features = features_by_dtype["float64"]
int_features = features_by_dtype["int64"]
numerical_features = float_features + int_features
remove_list = ["GarageYrBlt", "YearBuilt", "YearRemodAdd", "MoSold", "YrSold", "MSSubClass"]
numerical_features = [n for n in numerical_features if n not in remove_list]

