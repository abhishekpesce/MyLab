from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

from datetime import datetime

def _process():
        print("i have been called")

with DAG("my_python_dag",start_date=datetime(2021,1,1),schedule_interval='@daily',catchup=False) as dag:

    task_a=PythonOperator(
        task_id = "task_a",
        python_callable=_process
        
    )

    task_a 