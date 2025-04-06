import os
from airflow.utils.session import provide_session
from airflow.models import DagRun, TaskInstance

def check_dag_status(dag_id, task_id):
    from airflow.utils.session import provide_session
    from airflow.models import DagRun, TaskInstance

    @provide_session
    def _inner(session=None):
        result = {
            "dag_id": dag_id,
            "task_id": task_id,
            "dag_status": None,
            "task_status": None,
            "log_tail": [],
        }

        dag_run = session.query(DagRun).filter(
            DagRun.dag_id == dag_id
        ).order_by(DagRun.execution_date.desc()).first()

        if not dag_run:
            result["dag_status"] = "no_run"
            return result

        result["dag_status"] = dag_run.state

        ti = session.query(TaskInstance).filter(
            TaskInstance.dag_id == dag_id,
            TaskInstance.task_id == task_id,
            TaskInstance.execution_date == dag_run.execution_date
        ).first()

        if ti:
            result["task_status"] = ti.state

            # 로그 파일 경로 구성
            import os
            log_dir = os.getenv("AIRFLOW_HOME", os.path.expanduser("~/airflow"))
            log_path = os.path.join(
                log_dir, "logs", dag_id, task_id,
                dag_run.execution_date.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                "1.log"
            )

            try:
                with open(log_path, "r") as f:
                    result["log_tail"] = f.readlines()[-5:]
            except Exception as e:
                result["log_tail"] = [f"⚠️ Log read failed: {e}"]

        return result

    return _inner()
