import pickle
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler 

path = "../datasets/accepted_2007_to_2018Q4.csv"
df = pd.read_csv(path)
#use required features
features_to_use = ["loan_status","avg_fico_range", "total_rec_prncp", "last_pymnt_amnt", "grade", "home_ownership"]
features_selected_dataset = df[features_to_use]
ohe_dataset = pd.get_dummies(features_selected_dataset, drop_first = True)

X = ohe_dataset.drop('loan_status', axis=1)
y = ohe_dataset['loan_status']

scale = MinMaxScaler()

X_train= scale.fit_transform(X_train)
X_test = scale.transform(X_test)

rf = RandomForestClassifier()

rf.fit(X_train, y_train)

pickle.dump(rf, open(model.pkl),'wb')

model = pickel.load( open(model.pkl),'rb')

