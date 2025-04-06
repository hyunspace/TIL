from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time

def sleep_for_a_while():
    print("😴 Sleeping for 30 seconds...")
    time.sleep(30)
    print("🌞 Done sleeping!")

with DAG(
    dag_id="python_sleep_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["jhyun"],
) as dag:
    sleep_task = PythonOperator(
        task_id="sleep_task",
        python_callable=sleep_for_a_while,
    )
