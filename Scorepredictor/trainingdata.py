import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = {
    
    'attendance':      [90, 75, 85, 60, 95, 50, 80, 40, 100, 70],
    'assignment1_avg': [88, 72, 80, 58, 92, 55, 82, 42, 96, 68],
    'assignment2_avg': [88, 72, 80, 58, 92, 55, 82, 42, 96, 68],
    'final_score':     [90, 74, 80, 60, 95, 58, 85, 45, 98, 70]
}

df = pd.DataFrame(data)
inValues = df[['attendance', 'assignment1_avg', 'assignment2_avg']]
outValues = df['final_score']

model = LinearRegression()
model.fit(inValues, outValues)

with open('model1.pkl', 'wb') as f:
    pickle.dump(model, f)
