from flask import Flask, render_template, request, send_file
import pickle
import numpy as np
import io
import matplotlib.pyplot as plt
import base64


# Create Flask app for Score Prediction
app = Flask(__name__)

# Load the trained model that created with input data
with open('model1.pkl', 'rb') as f:
    model = pickle.load(f)

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    plot_url = None
    if request.method == 'POST':
         try: 
           attendance = float(request.form['attendance'])
           assignment1_avg = float(request.form['assignment1_avg'])
           assignment2_avg = float(request.form['assignment2_avg']) 
           input_data = np.array([[attendance, assignment1_avg,assignment2_avg]])
           prediction = model.predict(input_data)[0]
           labels = ['attendance', 'assignment1_avg', 'assignment2_avg', 'Predicted Score']
           values = [attendance, assignment1_avg,assignment2_avg, prediction]

           plt.figure(figsize=(8, 5))
           plt.bar(labels, values, color=['red', 'red', 'red', 'green'])
           plt.title('Student Prediction Overview')
           plt.ylabel('Score')
           plt.ylim(0, 100)
           plt.grid(True, axis='y')


           buf = io.BytesIO()
           plt.savefig(buf, format='png')
           buf.seek(0)
           plt.close()
           plot_url = base64.b64encode(buf.getvalue()).decode('utf8')

         except Exception as e:
            prediction = f"Error: {str(e)}"
            
    return render_template('index.html', prediction=prediction,plot_url=plot_url)
# Run the app
if __name__ == '__main__':
    app.run(debug=True)