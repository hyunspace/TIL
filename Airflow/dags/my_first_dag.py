from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def say_hello():
    print("Hello from Airflow DAG!")

with DAG(
    dag_id="my_first_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["jhyun"],
) as dag:
    task_hello = PythonOperator(
        task_id="say_hello_task",
        python_callable=say_hello,
    )