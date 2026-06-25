import json

from src.common.minio_client import get_minio_client


class BronzeSeasonReader:

    BUCKET = "bronze-raw"
    PREFIX = "seasons/"

    def __init__(self):
        self.client = get_minio_client()

    def get_latest_object_name(self):
        objects = list(
            self.client.list_objects(
                bucket_name=self.BUCKET,
                prefix=self.PREFIX,
                recursive=True,
            )
        )

        if not objects:
            raise FileNotFoundError(
                "Nenhum arquivo encontrado em bronze-raw/seasons"
            )

        latest_object = max(
            objects,
            key=lambda obj: obj.last_modified,
        )

        return latest_object.object_name

    def read_latest(self):
        object_name = self.get_latest_object_name()

        response = self.client.get_object(
            bucket_name=self.BUCKET,
            object_name=object_name,
        )

        try:
            data = json.loads(
                response.read().decode("utf-8")
            )
        finally:
            response.close()
            response.release_conn()

        return object_name, data