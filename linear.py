import pandas as pd

# import#

from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split, GridSearchCV
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
                          ('regressor', Ridge())])
    
    params = {'regressor__alpha':[0.1,0.3,0.5,0.8,1]}
    
    gs = GridSearchCV(reg,params,cv = 5)

    gs.fit(X_train, y_train)
    print('model score on training set = ',gs.score(X_train, y_train))
    print('model score on test set =',gs.score(X_test,y_test) )
    
    


def read_data(path):
    data = pd.read_excel(path)
    return data


main()
