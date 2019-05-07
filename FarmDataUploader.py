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

    trigger_url = 'https://functions-vivid.azurewebsites.net/api/HttpTrigger1?code=I3VJhugK6llvTNwAcNc53tRasmK/qKR0EXnOTccdc0Xcaw251w/bCw=='

    payload = {
        "ID": 12731,
        "lact_d": 10.0,
        "lact_n":10,
        "lbd_d": 64,
        "daily_prod": 12.31,
        "label": 0,
    }


    # GET with params in URL
    request1 = requests.get(trigger_url, params = payload)

    print(request1.text)
    print(request1.status_code)

if __name__ == "__main__":
    main(sys.argv)
