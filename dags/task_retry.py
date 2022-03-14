from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

from datetime import datetime,timedelta

with DAG("task_retry",start_date=datetime(2021,1,1),schedule_interval='@daily',catchup=False) as dag:

    task_a= BashOperator(
        #owner='john',
        task_id="task_a",
        bash_command="echo 'task_a'"
    )

    task_b= BashOperator(
        #owner='marc',
        task_id="task_b",
        retries=3,
        retry_exponential_backoff=True,
        retry_delay=timedelta(seconds=10),
        bash_command="echo 'task_b' && exit 1"
    )

task_a >> task_b