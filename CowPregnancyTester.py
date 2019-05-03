import requests, json
import os
import sys
import time
import json
import requests
import statistics

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
       "DATB_i": 446,
       "DIMB_i": 2233,
       "FAT": 247,
       "YEILD": 651,
       "LACTOSE": 793,
       "PROTEIN": 4440,
       "THI": 683.4889299143,
       "LACT": 339
    }
    lis = []
    for i in range(0,50):
        startTime = time.time()
        headers = {'Content-Type':'application/json'}
        resp = requests.post(trigger_url, json=testData, headers=headers)
        endTime = time.time()
        lis.append(endTime-startTime)
        #print(i)
        #print("POST to url", trigger_url)
        #print("prediction:", resp.text)
    print("Standard Deviation of sample is % s " % (statistics.stdev(lis)))
    print("Mean of sample is % s " % (statistics.mean(lis)))

if __name__ == "__main__":
    main(sys.argv)
