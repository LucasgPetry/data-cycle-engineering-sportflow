from minio_client import get_minio_client
from minio import S3Error
import time

BUCKETS = [
    "bronze-raw", 
    "silver-stagging", 
    "gold-export"
]

def wait_for_minio(client): 

    while True: 

        try: 
            client.list_buckets()
            return
        
        except Exception: 
            print("Aguardando Minio...")
            time.sleep(5)

def main(): 
    client = get_minio_client()

    wait_for_minio(client)

    for bucket in BUCKETS:

        if not client.bucket_exists(bucket): 
            client.make_bucket(bucket)
            print(f"Bucket criado: {bucket}")
        
        else: 
            print(f"Bucket já existe: {bucket}")
        
if __name__ == "__main__": 
    main()
