# Description
This is a web app that automatically runs basic exploratory data analysis for CSVs.
This app will parse strings, datetime and numeric types of data and quickly provide visualisations for a brief overview of the dataset.

# Authors
Matthew Moghaddam
Michelle Xiong
Shannon Murdoch
Stefan Hall

# Structure

# Instructions
To load this app, you will first need to initialise a docker image with the following command:

docker build -t [yourimagename]:latest .

eg:
    docker build -t automaticeda:latest .

This will build an image according to the specifications in the Dockerfile

Next we need to build a container from which to run the streamlit app. Use the following command:

docker run -dit --rm --name [yourcontainername] -p 8501:8501 -v "${PWD}":/app [yourimagename]:latest

eg:
    docker run -dit --rm --name containapp -p 8501:8501 -v "${PWD}":/app streamlitapp:latest

Lastly open a browser and navigate to http://localhost:8501 
From there you will be able to explore your data quickly and easily.