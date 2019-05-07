import os
import sys
import time
import json
import requests
import argparse

parser = argparse.ArgumentParser(description='batch farm data uploader')
parser.add_argument('--file', metavar='-f', type=str, help='file to load jsons from [required]')
args = parser.parse_args()

features = {
    "ID": "the cow id to which the row of data corresponds",
    "date": "current date",
    "lact_d": "days in lactation",
    "lact_n": "lactation number",
    "lbd": "last breeding date",
    "lbd_d" : "days since last breeding",
    "daily production" : "Milk yield",
    "label" : "pregnant or not",
}

def getListOfJsons(filepath = 'data.json'):
    """
    returns a list of json objects by reading them from the file passed as input argument
    """
    print("Loading JSONs...")
    try:
        with open(filepath) as f:
            data = json.load(f)
    except:
        print('Error occured in loading JSON, check filename')
        raise Exception()

    print("Loaded JSONs, processing payloads...")
    return processPayloads(data['data'])

def processPayloads(data_rows):
    """
    returns a list of payloads ready to be uploaded
    """
    payloads = []
    for row in data_rows:
        try :
            lbd = (
                int(row['date'][:2]) + 30 * int(row['date'][2:4]) + 365 * int(row['date'][4:])
                - int(row['lbd'][:2]) + 30 * int(row['lbd'][2:4]) + 365 * int(row['lbd'][4:])
                )
        except:
            print("Skipping! Error occured in parsing dates for cowID: ", row['ID'])
            continue
        payload = {
            "ID": row['ID'],
            "lact_d": row['lact_d'],
            "label": row['label'],
            "lact_n": row['lact_n'],
            "lbd_d": lbd,
            "daily_prod": row['daily_prod']
        }
        payloads.append(payload)
    print('Processed payloads')
    return payloads


def main(args):

    trigger_url = 'https://functions-vivid.azurewebsites.net/api/HttpTrigger1?code=I3VJhugK6llvTNwAcNc53tRasmK/qKR0EXnOTccdc0Xcaw251w/bCw=='

    try:
        payloads = getListOfJsons(args.file)
    except:
        print('Failed to upload!')
        return -1

    failures = []
    for payload in payloads:
        # GET with params in URL
        request1 = requests.get(trigger_url, params = payload)
        if request1.status_code!=200:
            failures.append(payload['ID'])

    if len(failures) == 0:
        print("Successfully uploaded " + str(len(payloads)) + " files")
    else:
        print("Failed upload for IDs:", failures)


if __name__ == "__main__":
    main(args)
