import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import numpy as np
import pandas as pd
import csv
import streamlit as st
from PIL import Image

st.write("""
# Shallow foundation bearing capacity prediction
This app predicts the **Ultimate Bearing Capacity of shallow foundation granular soil **!
""")
st.write('---')
image=Image.open(r'foundation.jpg')
st.image(image, use_column_width=True)

data = pd.read_csv(r"foundation1.csv")
req_col_names = ["B", "D", "LoverB", "gamma","degree","qu"]
curr_col_names = list(data.columns)

mapper = {}
for i, name in enumerate(curr_col_names):
    mapper[name] = req_col_names[i]

data = data.rename(columns=mapper)
st.subheader('data information')
data.head()
data.isna().sum()
corr = data.corr()
st.dataframe(data)
X = data.iloc[:,:-1]         # Features - All columns but last
y = data.iloc[:,-1]          # Target - Last Column
print(X)
from sklearn.model_selection import train_test_split
import pickle
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=0)

# Sample data (replace with your own data)
# X, y = your_features, your_labels

# Split the data

# Initialize and train the AdaBoostRegressor
model = GradientBoostingRegressor(learning_rate=0.5, n_estimators=100)
model.fit(X_train, y_train)
st.sidebar.header('Specify Input Parameters')
def get_input_features():
    B = st.sidebar.slider('B', 0.03,3.02,0.05)
    D = st.sidebar.slider('D',0.00,0.89,0.50)
    LoverB = st.sidebar.slider('LoverB', 1.00,6.00,3.00)
    gamma = st.sidebar.slider('gamma', 31.95,45.70,33.00)
    degree  = st.sidebar.slider('degree', 9.85,20.80,20.60)





    data_user = {'B': B,
            'D': D,
            'LoverB': LoverB,
            'gamma': gamma,
            'degree': degree,

    }
    features = pd.DataFrame(data_user, index=[0])
    return features

df = get_input_features()
# Main Panel

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')




# Reads in saved classification model
import pickle
load_clf = pickle.load(open('GBRT_model.pkl', 'rb'))
st.header('Prediction of qu (kPa)')

# Apply model to make predictions
prediction = load_clf.predict(df)
st.write(prediction)
st.write('---') 
