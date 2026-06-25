import json

from pathlib import Path
from datetime import datetime


class LocalStorage:

    def save(self, data):

        now = datetime.utcnow()

        directory = Path(
            f"data/bronze/competitions/"
            f"{now:%Y}/{now:%m}/{now:%d}"
        )

        directory.mkdir(
            parents=True,
            exist_ok=True
        )

        filename = (
            f"competitions_{now:%Y%m%d_%H%M%S}.json"
        )

        filepath = directory / filename

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        return filepath