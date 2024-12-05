from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load pre-trained components
model = joblib.load(r'.\model.pkl')
scaler = joblib.load(r'.\scaler.pkl')
label_encoder = joblib.load(r'.\label_encoder.pkl')

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input from the form
        input_data = [
            int(float(request.form['obj_ID'])),  # Corrected this line
            float(request.form['alpha']),
            float(request.form['delta']),
            float(request.form['u']),
            float(request.form['g']),
            float(request.form['r']),
            float(request.form['i']),
            float(request.form['z']),
            int(request.form['run_ID']),
            int(request.form['rerun_ID']),
            int(request.form['cam_col']),
            int(request.form['field_ID']),
            float(request.form['spec_obj_ID']),
            float(request.form['redshift']),
            int(request.form['plate']),
            int(request.form['MJD']),
            int(request.form['fiber_ID']),
        ]
        
        # Print the input data to the console
        print(input_data)

        # Uncomment the following code once you confirm the input data
        # Convert input to a NumPy array and scale it
        input_array = np.array(input_data).reshape(1, -1)
        scaled_input = scaler.transform(input_array)
        
        # Make prediction
        prediction = model.predict(scaled_input)
        predicted_label = label_encoder.inverse_transform(prediction)[0]
        
        return render_template('result.html', prediction=predicted_label)
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
