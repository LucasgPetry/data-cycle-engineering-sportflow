import json
from datetime import datetime
from io import BytesIO

from src.common.minio_client import get_minio_client


class TeamMinIOStorage:

    BUCKET = "bronze-raw"

    def save(self, data):
        client = get_minio_client()

        now = datetime.utcnow()

        object_name = (
            f"teams/"
            f"{now:%Y}/"
            f"{now:%m}/"
            f"{now:%d}/"
            f"teams_{now:%Y%m%d_%H%M%S}.json"
        )

        payload = json.dumps(
            data,
            ensure_ascii=False,
            indent=4,
        ).encode("utf-8")

        client.put_object(
            bucket_name=self.BUCKET,
            object_name=object_name,
            data=BytesIO(payload),
            length=len(payload),
            content_type="application/json",
        )

        return object_name