import pandas as pd
import os
 
 
class FeatureExtractor(object):
    def __init__(self):
        pass
 
    def fit(self, X_df, y_array):
        pass
 
    def transform(self, X_df):
        X_encoded = X_df
        
        #uncomment the line below in the submission
        path = os.path.dirname(__file__)
        special_days=pd.read_csv(os.path.join(path, "data_specialdays.csv"), sep = ';')
        distance=pd.read_csv(os.path.join(path, "Distance.csv"), sep = ';')
        air_fares=pd.read_csv(os.path.join(path, "Airfares.csv"), sep = ';')
        #special_days = pd.read_csv("data_specialdays.csv", sep = ';')
        #distance = pd.read_csv("Distance.csv",sep = ';')
        #air_fares = pd.read_csv("Airfares.csv",sep = ';')
        X_encoded = X_encoded.merge(special_days, how='left', left_on=['DateOfDeparture'], right_on=['DateOfDeparture'], sort=False)
        X_encoded = X_encoded.merge(distance, how='left', left_on=['Departure','Arrival'], right_on=['Departure','Arrival'], sort=False)

        X_encoded['DateOfDeparture'] = pd.to_datetime(X_encoded['DateOfDeparture'])
        X_encoded['year'] = X_encoded['DateOfDeparture'].dt.year
        X_encoded['month'] = X_encoded['DateOfDeparture'].dt.month
        X_encoded['weekday'] = X_encoded['DateOfDeparture'].dt.weekday
        X_encoded['week'] = X_encoded['DateOfDeparture'].dt.week
        X_encoded = X_encoded.merge(air_fares, how='left', left_on=['Departure', 'Arrival', 'year', 'month'], right_on=['Departure', 'Arrival', 'year', 'month'], sort=False)
                
        X_encoded = X_encoded.join(pd.get_dummies(X_encoded['year'], prefix='y'))
        X_encoded = X_encoded.join(pd.get_dummies(X_encoded['weekday'], prefix='wd'))
        X_encoded = X_encoded.join(pd.get_dummies(X_encoded['week'], prefix='w'))
        X_encoded = X_encoded.join(pd.get_dummies(X_encoded['Departure'], prefix='d'))
        X_encoded = X_encoded.join(pd.get_dummies(X_encoded['Arrival'], prefix='a'))
        X_encoded = X_encoded.drop('Departure', axis=1)
        X_encoded = X_encoded.drop('Arrival', axis=1)     
        X_encoded = X_encoded.drop('weekday', axis=1)
        X_encoded = X_encoded.drop('week', axis=1)
        X_encoded = X_encoded.drop('year', axis=1)
        X_encoded = X_encoded.drop('month', axis=1)
        X_encoded = X_encoded.drop('std_wtd', axis=1)
        X_encoded = X_encoded.drop('WeeksToDeparture', axis=1)        
        X_encoded = X_encoded.drop('DateOfDeparture', axis=1)
        X_encoded = X_encoded.drop('NYE', axis=1)
        X_encoded = X_encoded.drop('PRESIDENTSDAY', axis=1)
        X_encoded = X_encoded.drop('EASTER', axis=1)
        X_encoded = X_encoded.drop('MEMORIALDAY', axis=1)
        X_encoded = X_encoded.drop('INDEPENDANCEDAY', axis=1)
        X_encoded = X_encoded.drop('LABOURDAY', axis=1)
        X_encoded = X_encoded.drop('HALLOWEEN', axis=1)
        X_encoded = X_encoded.drop('TGV', axis=1)
        X_encoded = X_encoded.drop('XMAS', axis=1)
        X_array = X_encoded.values
        return X_array
