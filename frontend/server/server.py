from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world!"

@app.route("/house_price", methods=['POST'])
def house_price():
    CHAS = int(request.form['CHAS'])
    RM = int(request.form['RM'])
    PTRATIO = int(request.form['PTRATIO'])

    response = jsonify({
        'estimated_price' : utils.get_prediction(CHAS, RM, PTRATIO)
        })
    
    return response

if __name__ == "__main__":
    print("starting flask framework")
    utils.load_saved_artifacts()
    app.run()
