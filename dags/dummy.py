from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(2),
    'retries': 1
}

with DAG('example_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    # Define tasks
    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')
    task3 = DummyOperator(task_id='task3')

    # Define task dependencies
    
    task1 >> task2 >> task3
