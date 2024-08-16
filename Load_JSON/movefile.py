
def load_table_uri_json(table_id):

  from google.cloud import bigquery

#construct bigquery client
client = bigquery.Client()

table_id = 'wiseally-6996.bq_json.josn_load_bq'
job_config = bigquery.LoadJobConfig(
  schema=[
    bigquery.SchemaField("name","STRING"),
    bigquery.SchemaFiled("location","STRING")
  ],
  source_format=bigquery.SourceFormat.NEW_LINE_DELIMITED_JSON,
)
uri="gs://bigquery-demo-78907/data.json"

load_job=client.load_table_from_uri(
  uri,
  table_id,
  location="US" #match with the destination dataset location
  job_config=job_config,
)

load_job.result()

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))  
  
  
  
