import pickle
import json
import numpy as np

__locations = None
__data_col = None
__model = None

def get_price_estimate(Region, Total_Sqft, BHK, EMI_Starts):
    try:
        loc_index = __data_col.index(Region.lower())
    except ValueError:
        loc_index = -1

    a = np.zeros(len(__data_col))
    a[0] = Total_Sqft
    a[1] = BHK
    a[2] = EMI_Starts
    if loc_index >= 0:
        a[loc_index] = 1

    #print(f"Feature vector: {a}")  # Debug print

    try:
        prediction = __model.predict([a])[0]
        print(f"Prediction: {prediction}")  # Debug print
        return round(prediction, 2)
    except Exception as e:
        #print(f"Error in model prediction: {e}")
        return None

def get_location():
    return __locations

def load_saved_artifacts():
    print("loading.........begins")
    global __data_col
    global __locations
    global __model

    with open("./server/artifacts/columns.json", "r") as f:
        __data_col = json.load(f)['data_columns']
        __locations = __data_col[3:]

    with open("./server/artifacts/west_bengal_estate_price.pickle", "rb") as f:
        __model = pickle.load(f)
    
    print("loading........complete")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location())
    print(get_price_estimate('Agarpara', 1000, 2, 20000))
    print(get_price_estimate('Garia', 1200, 3, 20000))
    print(get_price_estimate('Rajdham', 1400, 3, 23000))  # random location