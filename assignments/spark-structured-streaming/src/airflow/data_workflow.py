"""
This Python script defines an Airflow DAG for a recipe ETL workflow.

The DAG consists of two main tasks:

1. Dataload: This task calls the `process_data` function (assumed to be defined in `pipelines.dataload`)
   to load raw data for recipe processing.
2. Prepare: This task calls the `preprocess_data` function (assumed to be defined in `pipelines.prepare`)
   to preprocess the loaded data to a destination like a database or data warehouse for further analysis.

The DAG has the following properties:
- Schedule interval: daily (meaning it will triggered at midnight (00:00) of each day)
- Owner: airflow
- Start date: 2023-05-01
- Email on failure/retry: Disabled
- Retry configuration: Retry once after 5 minutes on failure
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

from pipelines.dataload import process_data
from pipelines.prepare import preprocess_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG('recipe_etl', default_args=default_args, schedule_interval="@daily") as dag:
    dataload_task = PythonOperator(
        task_id='dataload',
        python_callable=process_data,
    )

    prepare_task = PythonOperator(
        task_id='prepare',
        python_callable=preprocess_data,
    )

    dataload_task >> prepare_task
