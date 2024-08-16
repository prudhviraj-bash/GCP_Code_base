
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
import datetime
from airflow.operators.python_operator import PythonOperator
from movefile import table_load_uri_json
from airflow.operators.bash_operator import BashOperator

table_id = ""

default_dag_args={
  'owner':'airflow',
  'email_on_failure':False,
  'email_on_retries':False,
  'start_date':days_ago(1),
  'retries':1,
  'retry_delay':datetime.timedelta(minutes=5)
}

with DAG(
  'loading-Json-from-GCS2BQ',
  schedule_interval=None,
  default_args=default_dag_args,
)as dag:
  start=DummyOperator(
    task_id='start'
  )
  load=PythonOperator(
    task_id='loading_json_to_BQ'
    python_callable=table_load_uri_json
  op_args=[table_id]
  )
  end=BashOperator(
    task_id='end'
    bash_command='echo "Successfully Loaded Json File from GCS to BQ"'
  )

start>>load>>end

