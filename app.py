import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from joblib import dump, load
app = Flask(__name__)
filename = "model.pkl"

with open(filename, 'rb') as file:
    model = load(file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    X_test_new = [x.strip() for x in request.form.values()]
    X_test_new[1] = float(X_test_new[1])
    X_test_new[2] = float(X_test_new[2])
    # final_features = [np.array(int_features)]
    # X_test_new = [x for x in request.form.values()]

    # # print(sgd_clf.predict(X_test_new_count))
    #
    ll = [X_test_new]
    new_data = pd.DataFrame(ll, columns=['Gas', 'Water_content', 'time_minutes'])
    prediction = model.predict(new_data)[0]
    output = round(prediction, 2)

    return render_template('index.html', prediction_text='Estimated IFT =  {} mN/m'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
