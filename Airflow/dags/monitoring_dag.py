from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.get_latest_dag_status import get_latest_dag_status

TARGET_DAG_ID = "python_sleep_dag"

#
def check_status_and_branch(**context):
    status = get_latest_dag_status(TARGET_DAG_ID)
    print(f"📡 Status of '{TARGET_DAG_ID}': {status}")

    if status == "success":
        print("✅ DAG B completed. Continuing...")
    elif status == "running":
        print("⏳ DAG B is still running. Exiting.")
        return
    elif status == "failed":
        raise Exception("❌ DAG B failed!! Stopping.")
    elif status == "no_run":
        print("🚫 No run found. Exiting.")
    else:
        print(f"⚠️ Unknown status: {status}")

with DAG(
    dag_id="monitoring_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["jhyun"],
) as dag:

    check = PythonOperator(
        task_id="check_dag_b_status",
        python_callable=check_status_and_branch,
        provide_context=True,
    )


# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime
# import os, sys
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# from utils.get_latest_dag_status import get_latest_dag_status

# TARGET_DAG_ID = "python_sleep_dag"

# def check_status_and_branch(**context):
#     status = get_latest_dag_status(TARGET_DAG_ID)
#     print(f"📡 Status of '{TARGET_DAG_ID}': {status}")

#     if status == "success":
#         print("✅ DAG B completed. Continuing...")
#     elif status == "running":
#         print("⏳ DAG B is still running. Exiting.")
#         return
#     elif status == "failed":
#         raise Exception("❌ DAG B failed! Stopping.")
#     elif status == "no_run":
#         print("🚫 No run found. Exiting.")
#     else:
#         print(f"⚠️ Unknown status: {status}")

# with DAG(
#     dag_id="monitoring_dag",
#     start_date=datetime(2024, 1, 1),
#     schedule_interval=None,
#     catchup=False,
#     tags=["jhyun"],
# ) as dag:

#     check = PythonOperator(
#         task_id="check_dag_b_status",
#         python_callable=check_status_and_branch,
#         provide_context=True,
#     )
