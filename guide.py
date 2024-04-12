import os
import boto3
import datetime
from config import load_env
from dateutil.tz import tzutc
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def download_folder(bucket_name, prefix, local_dir, access_key, secret_key, endpoint_url, region, date):
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, endpoint_url=endpoint_url, region_name=region)
    
    fromDate = datetime.datetime(*date, tzinfo=tzutc())
    print(fromDate)
    try:
        paginator = s3.get_paginator('list_objects_v2')
        operation_parameters = {'Bucket': bucket_name, 'Prefix': prefix}
        for page in paginator.paginate(**operation_parameters):
            for content in page.get('Contents', []):
                if content["LastModified"] > fromDate:
                    key = content['Key']
                    # Construct the local file path using the prefix and key
                    local_file_path = f"{local_dir}/{key[len(prefix):]}"
                    # Create the directories if they don't exist
                    local_file_dir = '/'.join(local_file_path.split('/')[:-1])
                    os.makedirs(local_file_dir, exist_ok=True)
                    # Download the file
                    s3.download_file(bucket_name, key, local_file_path)
                    print(f"Downloaded: {local_file_path}")

        print("Download completed!")
    except NoCredentialsError:
        print("Credentials not available.")
    except PartialCredentialsError:
        print("Partial credentials found.")

env = load_env({})
bucket_name = env["bucket_name"]
prefix = env["prefix"]
local_dir = env["local_dir"]
access_key = env["access_key"]
secret_key = env["secret_key"]
endpoint_url = env["endpoint_url"]
region = env["region"]
date = tuple(map(int, env["from_date"].split(", ")))

download_folder(bucket_name, prefix, local_dir, access_key, secret_key, endpoint_url, region, date)