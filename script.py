import pickle


client = {"job": "management", "duration": 400, "poutcome": "success"}


with open('model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)


with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)


X = dv.transform(client)

prob = model.predict_proba(X)[0, 1]

print(prob)
