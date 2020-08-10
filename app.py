import numpy as np
import time
import threading
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array(int_features)
    prediction = model.predict([final_features])
    predictionsProb =model.predict_proba([final_features])
    s=round(prediction[0])
    
    
    mk = predictionsProb[0,1]*100
  
    if s==1 :
     return render_template('index.html', prediction_text ='you are at risk of infection by diabete',  predictions_prob = 'with ratio  ',p = mk , per = '%')
    else:
     return render_template('index.html', prediction_text ='You are not threatened with diabete',  predictions_prob = 'with ratio  ',p = mk, per = '%')

   # output = round(prediction[0], 2)
   



if __name__ == "__main__":
    app.run(debug=True)
