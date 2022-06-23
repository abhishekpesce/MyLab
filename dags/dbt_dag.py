from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta
from airflow.providers.dbt.cloud.operators.dbt import (
    DbtCloudGetJobRunArtifactOperator,
    DbtCloudRunJobOperator,
)


with DAG(
    dag_id='dbt_dag',
    default_args={"dbt_cloud_conn_id": "dbt", "account_id": 76645}
    start_date=datetime(2021, 12, 23),
    description='An Airflow DAG to invoke simple dbt commands',
    schedule_interval=timedelta(days=1),
    catchup = False
) as dag:

    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='dbt run'
    )

    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='dbt test'
    )

    dbt_run >> dbt_test