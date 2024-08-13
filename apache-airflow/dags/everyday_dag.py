from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
import requests
from datetime import datetime

def _load_dog():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    pic = response.json()
    data = pic["message"]
    print(data)
    return data

default_args = {
    'start_date': datetime(2024, 7, 28)
}

dag = DAG(
    'dog',
    schedule_interval="@daily",
    default_args=default_args,
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)
    
load_dog = PythonOperator(
    task_id = "load_dog",
    python_callable = _load_dog,
    dag = dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

start >> load_dog >> end
