from google.cloud import storage


class UploadParquet:
    def __init__(self, bucket: str):
        self.client = storage.Client()
        self.bucket = self.client.bucket(bucket)

    def upload(self, source: str, target: str):
        blob = self.bucket.blob(target)
        blob.upload_from_filename(source)
