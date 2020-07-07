import json
import pickle
import numpy as np

data = None
model = None
mean = None



def get_prediction(CHAS, RM, PTRATIO):
    x = mean
    x[2] = CHAS
    x[4] = RM
    x[8] = PTRATIO
    
    return round((np.e** model.predict([x])[0] * 1000 * 27.5),0)


def load_saved_artifacts():
    global data
    global mean
    global model
    global CHAS
    global RM
    global PTRATIO 

    with open("artifacts/columns.json","r") as f:
        data = json.load(f)['data_columns']
        CHAS = data[2]
        RM   = data[4]
        PTRATIO = data[8]  

    with open("artifacts/mean.json",'r') as m:
        mean = json.load(m)['mean']

    with open("artifacts/boston_dataset.pickle", "rb") as f:
        model = pickle.load(f)
    print("loading model:")




if __name__ == "__main__":
    load_saved_artifacts()

