FROM apache/airflow:2.2.3
COPY requirements.txt .
RUN pip install --user --upgrade pip
RUN pip install -r requirements.txt