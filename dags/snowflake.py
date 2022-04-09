from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator

from datetime import datetime

with DAG("my_dag",start_date=datetime(2021,1,1),schedule_interval='@daily',catchup=False) as dag:

    task_a=DummyOperator(
        task_id="task_a"
    )

    task_b=DummyOperator(
        task_id="task_b"
    )

    task_a >> task_b