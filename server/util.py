import pickle
import json
import numpy as np

__locations =None
__data_col =None
__model= None

def get_price_estimate(Region,Total_Sqft,BHK,EMI_Starts):
    try:
        loc_index = __data_col.index(Region.lower())
    except:
        loc_index =-1

    a=np.zeros(len(__data_col))
    a[0]=EMI_Starts
    a[1]=BHK
    a[2]=Total_Sqft
    if loc_index >= 0:
        a[loc_index] = 1


    return round(__model.predict([a])[0],2)

def get_location():
    #pass
    return __locations

def load_saved_artifacts():
    print("loading.........begins")
    global __data_col
    global __locations
    
    
    with open("./server/artifacts/columns.json","r") as f:
        __data_col = json.load(f)['data_columns']
        __locations =__data_col[3:]

    global __model

    with open("./server/artifacts/west_bengal_estate_price.pickle","rb") as f:
        __model=pickle.load(f)
    
    print("loading........complete")



if __name__== '__main__':
    load_saved_artifacts()
    print(get_location())
    print("Prediction =",get_price_estimate('Agarpara',1000,2,20000))
    print("Prediction =",get_price_estimate('Garia',1200,3,20000))
    print("Prediction =",get_price_estimate('Rajdham',1400,3,23000)) #random location

