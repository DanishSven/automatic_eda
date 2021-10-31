# Project: automatic_eda
Collaborative Development of Data Explorer Web App

# Description
This is an interactive web application using Streamlit that that will read a provided CSV file by the user and perform basic exploratory data analysis on it.
This app will parse strings, datetime and numeric types of data and quickly provide visualisations for a brief overview of the dataset.

The web application will be composed of following 4 different sections:
1.	Overall information of the dataset
2.	Information on each numeric column
3.	Information on each text column
4.	Information on each datetime column

# Authors
Matthew Moghaddam,
Michelle Xiong,
Shannon Murdoch,
Stefan Hall

# Structure
    ├── streamlit_app.py   <- main application used for executing Streamlit
    ├── data.py            <- python script that will contain the code for overall information of the CSV file 
    ├── datetime.py        <- python script that will contain the code for information on each datetime column 
    ├── numeric.py         <- python script that will contain the code for information on each numeric column 
    ├── text.py            <- python script that will contain the code for information on each text column 
    ├── test_data.py       <- python script for testing code from data.py
    ├── test_datetime.py   <- python script for testing code from datetime.py
    ├── test_numeric.py    <- python script for testing code from numeric.py
    ├── test_text.py       <- python script for testing code from text.py
    ├── README.md          <- contains the information for the user about the project and code
    ├── requirements.txt   <- contains the python package requirements for the docker image to load
    ├── Dockerfile         <- contains the information to load a docker image
    └── docker-compose.yml <- contains the information


# Built With
Docker
Python 3.8.2
Streamlit 1.0.0
Numpy 1.21.3
Pandas 1.3.3


# Instructions
To load this app, you will first need to initialise a docker image with the following command:

docker build -t [yourimagename]:latest .

eg:
    docker build -t automaticeda:latest .

This will build an image according to the specifications in the Dockerfile

Next we need to build a container from which to run the streamlit app. Use the following command:

docker run -dit --rm --name [yourcontainername] -p 8501:8501 -v "${PWD}":/app [yourimagename]:latest

eg:
    docker run -dit --rm --name containapp -p 8501:8501 -v "${PWD}":/app automaticeda:latest

Lastly open a browser and navigate to http://localhost:8501 
From there you will be able to explore your data quickly and easily.

