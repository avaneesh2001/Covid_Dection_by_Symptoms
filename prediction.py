import numpy as np
import pandas as pd
import joblib

print('---------------Model to determine Covid 19 from symptums------------------------')
print('Model accuracy is 96.7%')
print('\n\nEnter the details: ')

abv60 = input('Are you above 60?(yes/no only) ')
if abv60 == 'yes':
    abv60 = 1
else:
    abv60 = 0

Sex = input('What is your gender?(male/female) ')
if Sex == 'male':
    Sex = 1
else:
    Sex = 0

Abroad = input('Have you been abroad?(yes/no only) ')
if Abroad == 'yes':
    Abroad = 1
else:
    Abroad = 0

print('Are you experiencing the following?')
head = input('Head aches?(yes/no only) ')
if head == 'yes':
    head = 1
else:
    head = 0

shortness_breath = input('shortness of breath?(yes/no only) ')
if shortness_breath == 'yes':
    shortness_breath = 1
else:
    shortness_breath = 0

Fever = input('Fever?(yes/no only) ')
if Fever == 'yes':
    Fever = 1
else:
    Fever = 0

Cough = input('Cough?(yes/no only) ')
if Cough == 'yes':
    Cough = 1
else:
    Cough = 0

soreThroat  = input('Sore Throat ?(yes/no only) ')
if soreThroat  == 'yes':
    soreThroat  = 1
else:
    soreThroat  = 0

contact  = input('Have you been in contact with covid patient?(yes/no only) ')
if soreThroat  == 'yes':
    contact  = 1
else:
    contact  = 0

from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators = 100)
forest = joblib.load("./random_forest.joblib")

x_test = [[Abroad,contact,Sex,abv60,head,shortness_breath,soreThroat,Fever,Cough]]
y_pred = forest.predict(x_test)
print('Your prediction is: ',y_pred)
if y_pred[0] == 0:
    print("\n\nYou most likely DONT have covid19")
else:
    print("\n\nYou most likely DO have covid19")
