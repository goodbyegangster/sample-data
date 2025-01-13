from google.cloud import bigquery


class LoadParquet:
    def __init__(self, project: str, region: str):
        self.client = bigquery.Client()
        self.project = project
        self.region = region

    def load(self, gcs: str, schema: str, table: str):
        schema = f"aw_{schema}"
        data_ids = [datasets.dataset_id for datasets in self.client.list_datasets()]
        if schema not in data_ids:
            dataset = bigquery.Dataset(".".join([self.project, schema]))
            dataset.location = self.region
            dataset.is_case_insensitive = False
            self.client.create_dataset(dataset=dataset)

        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.PARQUET, write_disposition="WRITE_TRUNCATE"
        )

        load_job = self.client.load_table_from_uri(
            source_uris=gcs,
            destination=".".join([self.project, schema, table]),
            job_config=job_config,
        )
        load_job.result()
