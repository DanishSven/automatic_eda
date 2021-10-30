FROM python:3.8.2

COPY requirements.txt .
COPY docker-compose.yml .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app
COPY . /src

WORKDIR /app

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["app/streamlit_app.py"]
