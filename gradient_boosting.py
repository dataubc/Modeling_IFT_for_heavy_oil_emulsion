import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def main(path = 'data/ift_data.xlsx', test_size = 0.2 ):
    
    '''
    building model tp predict the IFT when a gas is injected into heavy oil emulsion. The model predict the IFT given
    the type of the gas, water content in the emulsion (fraction) and time elapsed since gas injection
    
    inputs:
    ------
    - path : path to the input data, excel file that has the following input columns
       Gas : Categorical variable, the type of the gas injected into the emlusion
       Water_content : water fraction in the emulsion
      time_minutes : time elapsed since gas injection
      IFT: readings of the IFT in  mN/m
      volume_ratio: volume change since (fraction)
      
    - test_size : the size of the data set the will be allocated for testing
    
    
    outputs:
    ------
    None, the model print the score of the model in the training and test data set
    '''
    
    data = read_data(path)
    x = data.iloc[:,:3]
    y = data.iloc[:,4]
    
    # splitting the data 
    X_train, X_test,y_train, y_test = train_test_split(x,y,test_size = test_size)
    
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