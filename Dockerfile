FROM python:3.8.2
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8501
COPY . /app
ENTRYPOINT ["streamlit", "run"]
CMD ["app/streamlit_app.py"]
