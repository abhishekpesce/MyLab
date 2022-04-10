from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator

from datetime import datetime

query_test = """select current_date() as date;"""

with DAG("snowflake",start_date=datetime(2021,1,1),schedule_interval='@daily',catchup=False) as dag:

    snowflake = SnowflakeOperator(
    task_id='test_snowflake_connection',
    sql=query_test,
    snowflake_conn_id='snowflake_conn',
    dag=dag
    )

    task_a=DummyOperator(
        task_id="task_a"
    )

task_a >> snowflake