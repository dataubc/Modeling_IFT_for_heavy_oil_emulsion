import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.ensemble import GradientBoostingRegressor

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def main():
    
    data = read_data('data/ift_data.xlsx')
    x = data.iloc[:,:3]
    y = data.iloc[:,4]
    
    # splitting the data 
    X_train, X_test,y_train, y_test = train_test_split(x,y,test_size = 0.2)
    
    # create a transformer for categorical and numerical features
    
    categorical_features = ['Gas']
    
    categorical_transformer = Pipeline(steps = [('imputer',SimpleImputer(strategy = 'constant')),
                                                ('encoder',OneHotEncoder())])
    
    numerical_features = ['Water_content','time_minutes']
    
    numerical_transformer = Pipeline(steps = [('imputer',SimpleImputer()),
                                             ('scaler',StandardScaler())])
    
    preprocessor = ColumnTransformer(transformers = [('cat',categorical_transformer,categorical_features),
                                                  ('num',numerical_transformer,numerical_features)])
    
    regressor = GradientBoostingRegressor()
    
    regressor_pipeline = Pipeline(steps = [('preprocessor',preprocessor),
                                          ('regressor',regressor)])
    
    params = {'regressor__learning_rate':[0.1,0.4,0.6,0.8,1]}
    gs = GridSearchCV(regressor_pipeline,params,cv = 5)
    gs.fit(X_train,y_train)
    print('model score on training set = ',gs.score(X_train,y_train))
    print('model score on test set = ',gs.score(X_test,y_test))
    
    

def read_data(path):
    data = pd.read_excel(path)
    
    return data
    
    

main()