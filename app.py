from model.network import Net
from flask import Flask, jsonify, render_template, request
from preprocessing import *
import json

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/digit_prediction', methods=['POST'])


def digit_prediction():
    if(request.method == "POST"):
        img = request.get_json()
        img = preprocess(img)
        net = Net()
        digit, probability = net.predict_with_pretrained_weights(img, 'pretrained_weights.pkl')
        data = { "digit":int(digit), "probability":float(int(probability*100))/100. }
        # print(data)
        # for k,v in dpipata.items():
        #     if( isinstance(v,np.int64)):
        #         data[k]=int(v)
        return jsonify(data)
        

if __name__ == "__main__":
    app.run(debug=True)

