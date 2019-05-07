import requests, json
import os
import sys
import time
import json
import requests

'''
    TODO:
        1. Pass features as an argument
        2. Pass object name as an argument

        https://docs.microsoft.com/en-us/azure/azure-functions/functions-integrate-store-unstructured-data-cosmosdb?tabs=csharp
'''

features = {
    "ID": "the cow id to which the row of data corresponds",
    "DATB_i": "ith breeding date",
    "DIMB_i": "days in milk on ith breeding date",
    "LACT" : "Number of days in lactation",
    "YIELD" : "Milk yield",
    "FAT" : "fat content in the milk",
    "PROTEIN" : "protein content in the milk",
    "LACTOSE": "Lactose content in milk",
    "THI" : "Temperature Humidity Index"
}

def main(argv):

    trigger_url = 'https://cowpregpedictor.azurewebsites.net/api/predictionTrigger?code=6wJ58iIIT5IbG5dUHd1QkvNjWTcnt8XwX3wmvTKgcbD2aMJkC3dHkA=='



    testData = {
        "daily_prod": 41,
        "lact_d": 34,
        "lact_n": 1,
        "lbd_d": 12,
    }


    headers = {'Content-Type':'application/json'}
    resp = requests.post(trigger_url, json=testData, headers=headers)

    print("POST to url", trigger_url)
    print("prediction:", resp.text)

if __name__ == "__main__":
    main(sys.argv)
