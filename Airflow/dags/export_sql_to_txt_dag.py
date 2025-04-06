from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
import os

def export_to_txt():
    try:
        # PostgreSQL 연결
        engine = create_engine("postgresql+psycopg2://admin:admin@localhost/airflow")

        # 쿼리 실행
        sql = "SELECT * FROM example_data;"  # 💡 필요 시 변경
        with engine.connect() as conn:
            df = pd.read_sql(sql, con=conn)

        # 파일 저장 경로
        file_dir = os.path.expanduser("~/Desktop")
        file_path = os.path.join(file_dir, "export_result.txt")

        # 파일로 저장
        df.to_csv(file_path, index=False, sep="\t")
        print(f"✅ File saved at: {file_path}")

    except Exception as e:
        print("❌ Error occurred:", str(e))
        raise

with DAG(
    dag_id="export_sql_to_txt_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["export", "db", "jhyun"]
) as dag:

    export_task = PythonOperator(
        task_id="export_db_data_to_text",
        python_callable=export_to_txt,
    )
