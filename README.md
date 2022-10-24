# api-real-estate-predictor

## Description
The repository containt all the files and script necessary in order to predict
Belgium real estate price. the Model was train on data scraped from Immoweb and these data
are synthetise in 3 json files. The app.py file execute the main script and generate a http interface framed by fastapi.
Then to make it avaible to everyone, this script is transform in Docker format and host on Render.

## Installation
You need to install python 3.10 and all the package define in the requirements.txt file, or just try the 
Render link share in the Usage section.

## Usage
The program can give some inside on the Belgium real estate price (area and position impacts), but keep in mind that's not a price advise
for sellers or buyers.

[API Price Prediction Link](https://api-demo-real-estate-predictor-av.onrender.com)