from flask import Flask, request, jsonify
import pickle


with open('model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)

with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)


app = Flask('model')


@app.route('/predict', methods = ['POST'])
def predict():
    client = request.get_json()
    X = dv.transform(client)
    y_pred = model.predict_proba(X)[0, 1]
    sub = y_pred >= 0.5

    result = {
        'sub_prob' : float(y_pred),
        'sub' : bool(sub)
    }

    return jsonify(result)
