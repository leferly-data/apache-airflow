from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG("Bash_Operator") as dag:
    echo_hello = BashOperator(
        task_id = "Bash_Operator",
        bash_command="ls",
    )