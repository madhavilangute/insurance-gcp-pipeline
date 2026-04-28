from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def test_connection():
    print("Connectivity Test Successful: DAG is running!")

with DAG(
    dag_id='github_to_composer_test',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    task_test = PythonOperator(
        task_id='print_test',
        python_callable=test_connection
    )