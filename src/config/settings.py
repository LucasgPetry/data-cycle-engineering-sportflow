from dotenv import load_dotenv
import os

load_dotenv()

SPORTSMONKS_API_TOKEN = os.getenv(
    "SPORTSMONKS_API_TOKEN"
)

MINIO_ENDPOINT = os.getenv(
    "MINIO_ENDPOINT"
)

MINIO_ACCESS_KEY = os.getenv(
    "MINIO_ROOT_USER"
)

MINIO_SECRET_KEY = os.getenv(
    "MINIO_ROOT_PASSWORD"
)

POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")