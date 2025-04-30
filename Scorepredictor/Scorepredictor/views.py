from flask import Flask, render_template, request
import pickle
import numpy as np
# Create Flask app for Score Prediction
app = Flask(__name__)

# Load the trained model that created with input data
with open('model1.pkl', 'rb') as f:
    model = pickle.load(f)

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        attendance = float(request.form['attendance'])
        assignment1_avg = float(request.form['assignment1_avg'])
        assignment2_avg = float(request.form['assignment2_avg']) 
        input_data = np.array([[attendance, assignment1_avg,assignment2_avg]])
        prediction = model.predict(input_data)[0]
    
    return render_template('index.html', prediction=prediction)
# Run the app
if __name__ == '__main__':
    app.run(debug=True)