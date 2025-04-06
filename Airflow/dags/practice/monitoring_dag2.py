from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_done():
    print("✅ B DAG has completed successfully!")

def print_fail():
    print("❌ B DAG failed. Stopping workflow.")

def skip_if_failed(context):
    raise Exception("Skipping downstream tasks because B DAG failed.")

def print_start():
    print("🚀 Monitoring DAG has started!")

with DAG(
    dag_id="monitoring_dag2",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["jhyun"],
) as dag:

    start = PythonOperator(
        task_id="print_start",
        python_callable=print_start
    )

    trigger_b = TriggerDagRunOperator(
        task_id="trigger_b_dag",
        trigger_dag_id="python_sleep_dag",   # ✅ 여기에 트리거할 DAG ID 적기
        wait_for_completion=True,            # ✅ 끝날 때까지 기다림
        poke_interval=5,                     # ✅ 5초 간격으로 상태 확인
        allowed_states=["success"],          # ✅ 성공해야 다음 태스크 실행됨
        failed_states=["failed"],            # ✅ 실패하면 downstream 막힘
        reset_dag_run=True                   # ✅ 기존 실행 내역 무시하고 새로 실행
    )

    after_success = PythonOperator(
        task_id="after_success",
        python_callable=print_done
    )

    after_failure = PythonOperator(
        task_id="after_failure",
        python_callable=print_fail,
        trigger_rule="one_failed"
    )

    start >> trigger_b >> [after_success, after_failure]
