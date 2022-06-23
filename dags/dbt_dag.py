from datetime import datetime

from airflow.models import DAG

try:
    from airflow.operators.empty import EmptyOperator
except ModuleNotFoundError:
    from airflow.operators.dummy import DummyOperator as EmptyOperator  # type: ignore

from airflow.providers.dbt.cloud.operators.dbt import (
    DbtCloudGetJobRunArtifactOperator,
    DbtCloudRunJobOperator,
)
from airflow.providers.dbt.cloud.sensors.dbt import DbtCloudJobRunSensor
from airflow.utils.edgemodifier import Label
from tests.system.utils import get_test_env_id

ENV_ID = get_test_env_id()

DAG_ID = "dbt_cloud"


with DAG(
    dag_id=DAG_ID,
    default_args={"dbt_cloud_conn_id": "dbt", "account_id": 76645},
    start_date=datetime(2021, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
  begin = EmptyOperator(task_id="begin")

    end = EmptyOperator(task_id="end")

    # [START howto_operator_dbt_cloud_run_job]
    trigger_job_run1 = DbtCloudRunJobOperator(
        task_id="trigger_job_run1",
        job_id=98266,
        check_interval=10,
        timeout=300,
    )
    # [END howto_operator_dbt_cloud_run_job]

    # [START howto_operator_dbt_cloud_get_artifact]
    get_run_results_artifact = DbtCloudGetJobRunArtifactOperator(
        task_id="get_run_results_artifact", run_id=trigger_job_run1.output, path="run_results.json"
    )
    # [END howto_operator_dbt_cloud_get_artifact]

    begin >> Label("No async wait") >> trigger_job_run1 >> get_run_results_artifact>> end

    # Task dependency created via `XComArgs`:
    # trigger_job_run1 >> get_run_results_artifact
    # trigger_job_run2 >> job_run_sensor

    from tests.system.utils.watcher import watcher

    # This test needs watcher in order to properly mark success/failure
    # when "tearDown" task with trigger rule is part of the DAG
    list(dag.tasks) >> watcher()


from tests.system.utils import get_test_run  # noqa: E402

# Needed to run the example DAG with pytest (see: tests/system/README.md#run_via_pytest)
[docs]test_run = get_test_run(dag)
