from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime
from utils import check_dag_status2

def check_and_act(**kwargs):
    status = check_dag_status2("python_sleep_dag", task_id="sleep_task")

    print(f"💡 대상 DAG 상태: {status}")

    if status == "running":
        print("💤 아직 실행 중이에요!")
        return "STOP"

    elif status == "success":
        print("🎉 성공했으니 다음 단계로 진행!")
        return "TRIGGER_NEXT"

    elif status == "failed":
        print("💥 실패했어요. DAG 종료합니다.")
        return "STOP"

    else:
        print("❓ 상태 확인 불가 or 아직 실행 안 됨.")
        return "STOP"

with DAG(
    dag_id="monitoring_dag_bk",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["jhyun"],
) as dag:

    check_status = PythonOperator(
        task_id="check_sleep_dag_status",
        python_callable=check_and_act,
        provide_context=True,
    )

    trigger_followup = TriggerDagRunOperator(
        task_id="task_hello",
        trigger_dag_id="my_first_dag",  # 다음 실행할 대상
        wait_for_completion=False,
    )

    check_status >> trigger_followup
