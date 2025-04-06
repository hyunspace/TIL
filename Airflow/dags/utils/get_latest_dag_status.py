from airflow.models import DagRun
from airflow.utils.session import provide_session

@provide_session
def get_latest_dag_status(dag_id, session=None):
    latest_run = session.query(DagRun)\
        .filter(DagRun.dag_id == dag_id)\
        .order_by(DagRun.execution_date.desc())\
        .first()

    if not latest_run:
        return "no_run"

    return latest_run.state


# from airflow.models import DagRun
# from airflow.utils.session import provide_session
# from airflow.utils.state import State

# @provide_session
# def get_latest_dag_status(dag_id, session=None):
#     latest_run = session.query(DagRun)\
#         .filter(DagRun.dag_id == dag_id)\
#         .order_by(DagRun.execution_date.desc())\
#         .first()

#     if not latest_run:
#         return "no_run"

#     return latest_run.state
