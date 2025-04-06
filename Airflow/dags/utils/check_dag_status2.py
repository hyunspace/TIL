from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.api.common.experimental.get_task_instance import get_task_instance
from airflow.utils.state import State
from airflow.models import DagRun
from airflow.utils.session import provide_session
from datetime import datetime
import time

TARGET_DAG_ID = "python_sleep_dag"

@provide_session
def check_dag_status(session=None, **context):
    while True:
        dag_runs = session.query(DagRun).filter(DagRun.dag_id == TARGET_DAG_ID).order_by(DagRun.execution_date.desc()).all()

        if not dag_runs:
            print("🔍 No DAG runs found for", TARGET_DAG_ID)
            return

        latest = dag_runs[0]
        status = latest.state
        print(f"📡 Current Status of '{TARGET_DAG_ID}': {status}")

        if status == State.RUNNING:
            print("⏳ Still running... check again in 5 seconds.")
            time.sleep(5)
        elif status == State.SUCCESS:
            print("✅ Success! Proceeding.")
            return
        elif status == State.FAILED:
            raise Exception("❌ Failed! Stopping.")
        else:
            raise Exception(f"⚠️ Unexpected status: {status}")

with DAG(
    dag_id="check_dag_status2",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["monitoring", "jhyun"],
) as dag:

    check_status = PythonOperator(
        task_id="check_sleep_dag_live_status",
        python_callable=check_dag_status,
        provide_context=True,
    )
