# 표준 라이브러리 (Python 내장 모듈)
import logging
import pendulum
from datetime import datetime, timedelta
import os

# 서드파티 라이브러리 (설치 필요)
import oracledb
import pandas as pd

# Airflow 관련 모듈 (Airflow 전용 라이브러리)
from airflow import DAG
from airflow.providers.oracle.hooks.oracle import OracleHook
from airflow.operators.python import PythonOperator
from airflow.models import DagRun, TaskInstance
from airflow.utils.state import State
from datetime import datetime, timedelta
from airflow.utils.dates import timezone

def check_other_dag_status(**kwargs):
    from airflow.utils.session import provide_session
    from airflow.models import DagRun, TaskInstance

    dag_id = 'my_first_dag'
    task_id = 'say_hello_task'

    @provide_session
    def _inner(session=None):
        dag_run = session.query(DagRun).filter(
            DagRun.dag_id == dag_id
        ).order_by(DagRun.execution_date.desc()).first()

        if not dag_run:
            print(f"No runs found for {dag_id}")
            return

        print(f"🗂 DAG ID: {dag_id}")
        print(f"📅 Run Date: {dag_run.execution_date}")
        print(f"🚦 Status: {dag_run.state}")

        ti = session.query(TaskInstance).filter(
            TaskInstance.dag_id == dag_id,
            TaskInstance.task_id == task_id,
            TaskInstance.execution_date == dag_run.execution_date
        ).first()

        if ti:
            print(f"📌 Task: {task_id}")
            print(f"🔍 Task Status: {ti.state}")
            print(f"🕒 Start Time: {ti.start_date}")
            print(f"🕛 End Time: {ti.end_date}")

            # ✅ 로그 파일 경로 수동 구성
            airflow_home = os.getenv("AIRFLOW_HOME", os.path.expanduser("~/airflow"))
            log_path = os.path.join(
                airflow_home,
                "logs",
                dag_id,
                task_id,
                dag_run.execution_date.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                "1.log"  # 첫 실행 기준
            )

            print(f"📂 Log file path: {log_path}")
            try:
                with open(log_path, 'r') as f:
                    lines = f.readlines()
                    last_lines = lines[-5:]
                    print("📝 Last 5 log lines:")
                    for line in last_lines:
                        print(line.strip())
            except Exception as e:
                print(f"⚠️ 로그 파일을 읽을 수 없습니다: {e}")

    _inner()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='dag_checker',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=["jhyun"],
) as dag:

    monitor = PythonOperator(
        task_id='check_status_and_log',
        python_callable=check_other_dag_status,
        provide_context=True,
    )
