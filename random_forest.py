## This contains a function

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

data = pd.read_csv('data/data.csv')
x = data.iloc[:,1:-1].values
y = data.iloc[:,-1].values

from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators = 100)
forest.fit(x, y)
print('Done fitting')
print('Creating joblib')
joblib.dump(forest, "./random_forest.joblib")

print('Done')
