# Project: automatic_eda
Collaborative Development of Data Explorer Web App

# Description
<<<<<<< HEAD
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
    ├── requirements.txt   <- contains the information
    ├── Dockerfile         <- contains the information
    └── docker-compose.yml <- contains the information

# Built With
Python 3.8.2
=======
This is an interactive web application using Streamlit that that will read a provided CSV file by the user and perform basic exploratory data analysis on it. This app will parse strings, datetime and numeric types of data and quickly provide visualisations for a brief overview of the dataset.

The web application will be composed of following 4 different sections:

1- Overall information of the dataset
2- Information on each numeric column
3- Information on each text column
4- Information on each datetime column

# Authors
Matthew Moghaddam
Michelle Xiong
Shannon Murdoch
Stefan Hall

# Built With
Python 3.8.2

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
├── requirements.txt   <- contains the information
├── Dockerfile         <- contains the information
└── docker-compose.yml <- contains the information
>>>>>>> 1734c97d21123cc2023e3801b223ac5b31868d38

# Instructions
pip install -r requirements.txt
streamlit run streamlit_app.py
