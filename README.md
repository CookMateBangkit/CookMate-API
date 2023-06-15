# CookMate-API


## Link Website
https://cookmate-sm5m2qi7wa-as.a.run.app/

## Table Of Content
+ [API Description](#api-description)
+ [Installation Requirements](#installation-requirements)
+ [How to use](#how-to-use)
+ [Author](#author)

## API Description
Cookmate-API is an Application Programming Interface (API) that provides services for the Cookmate application. 
the following are the services provided by Cookmate-API: 

  1. Send pictures of ingredients to find food recipes
  2. Send a list of ingredients to find food recipes
  3. Search for food recipes 
  4. Displaying food ingredients

## Installation Requirements
  1. Python : https://www.python.org/downloads/
  2. Account Google Cloud Platform https://console.cloud.google.com/
  3. Docker Desktop https://www.docker.com/ (if you don't want to install all python dependencies)

## How to use
### The first thing you do
  1. Download the zip file on https://github.com/CookMateBangkit/CookMate-API/archive/refs/heads/main.zip
  2. If you don't want to dowload you can clone the github at https://github.com/CookMateBangkit/CookMate-API.git
  3. Download Ml Model at https://storage.googleapis.com/model-image-cookmate/model_capstone.h5 
  4. Save the model in the same directory as the Cookmate-API repository

### On local computer
  1. Make sure you have downloaded the Cookmate-API repository
  2. Make sure you have also downloaded the ML model and saved it in the Cookmate-API repository.
  3. Make sure you have also downloaded python and the required dependencies in requirements.txt
  4. Open CLI and direct to this repository
  5. Run the command `uvicorn --host 0.0.0.0 --port 8050 main:app`

### On the internet
  1. You can use the link directly `https://cookmate-sm5m2qi7wa-as.a.run.app/`

### With Docker
  1. Make sure you have installed Docker Desktop on your local computer. 
  2. Make sure you have downloaded or cloned the Cookmate-API repository
  3. Also make sure you have downloaded the ML model and saved it in one Cookmate-API repository.
  4. Open CLI and direct to this repository
  5. Run the command `docker build -t Cookmate-api:v1`
  6. Wait for the docker build to complete
  7. Next run the command `docker run -d -p 8050:8050 --name Cookmate-API Cookmate-API:v1`
  8. now the API runs on `http://localhost:8050/` and `http://0.0.0.0:8050/` 

### With GCP
  1. Open the cloud shell, then clone the CookMate-API repository
  2. Input the machine learning model into the repository
  3. Make sure you have given the cloud run admin role in the service account
  4. Pass iam-policy to project id `gcloud projects get-iam-policy <your project id>`
  5. Make sure the Service account Cloud run account permissions in Cloud Build are enabled
  6. Run the command `gcloud builds submit .`

## Author
+ Mohammad Faraditya Eka Putra
+ Ardana Aldhizuma Nugraha

