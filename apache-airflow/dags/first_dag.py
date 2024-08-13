from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def _frist_task():
    print("Hello apache")

dag = DAG('hello_dag')

hello_task = PythonOperator(
    task_id='first_task',
    python_callable=_frist_task,
    dag=dag,
)

