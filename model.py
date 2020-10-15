import pandas as pd

# import#

from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


# reg = Pipeline(steps = list of tuples)


def main():
    df = read_data('data/ift_data.xlsx')
    y = df[['IFT']]
    x = df[['time_minutes', 'Gas', 'Water_content']]
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    numeric_features = ['Water_content', 'time_minutes']
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())])

    categorical_features = ['Gas']
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    preprocessor = ColumnTransformer(transformers = [('num',numeric_transformer,numeric_features),
                                                    ('cat',categorical_transformer,categorical_features)])

    # Append classifier to preprocessing pipeline.
    # Now we have a full prediction pipeline.
    reg = Pipeline(steps=[('preprocessor', preprocessor),
                          ('Regressor', Ridge())])

    reg.fit(X_train, y_train)
    print("model score: %.3f" % reg.score(X_test, y_test))


def read_data(path):
    data = pd.read_excel(path)
    return data


main()
