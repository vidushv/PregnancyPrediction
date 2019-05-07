# PregnancyPrediction
This repository contains the code for a scalable system for predicting pregnancy in cows in farms across the nation. 

There are several components to this project which are listed as follows.

## UI
The UI portion of this project is contained in `dataUploaderUI.py` and `pregnancyTesterUI.py` which are UIs for the data uploader portion of the project and the inference portion of the project, respectively. 

## Function Servers
The function servers for this project are deployed on Microsoft Azure. Copies of the running code are provided in `dataUploader.csx` and `pregPredictor.csx`. These function servers interface with their respective UI portions.

## Python Scripts
Apart from the UI option, the farmers are provided with python scripts to accomplish the same functionality as well. `FarmDataBatchUploader.py` uploads batches of data that the farmer specifies to the Cosmos DB on Azure. `CowPregnancyTester.py` returns pregnancy predictions for a cow when the correct features are passed in by interfacing with the containerized ML model on Azure.

## Machine Learning Model
Our ML model uses random forests and is deployed on Azure through a callable containerized web service. The code for the ML model which produces 89% accuracy on the given data set is contained in `MLModel.ipynb`.

## Data
All data for model training and validation is contained in `data.csv`.

## Dependencies 
The code in this repository is written in python3 and C#. In order to execute the python portion of the project, the following dependencies must be installed.

* pandas
* sklearn
* tkinter
* requests
* os 
* threading
