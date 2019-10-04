import boto3
import json
import logging
import tarfile
import os
from datetime import datetime
from core.config import CONFIG_FILE_PATH, is_in_testing_mode
from core.s3_uploader import S3Uploader
from core.make_backup_tar import MakeBackups
from core.dummy_client import DummyClient

logging.basicConfig(
    format='%(asctime)s == %(levelname)s == %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO
)

bucket_name = 'wiki-documentation'
bucket_path = 'backups'
filename_path = '/Users/damien/app.log'
lifeclycle_policy = json.load(open(CONFIG_FILE_PATH))
tarfile_name = 'app.tar.gz'

def make_backup() -> MakeBackups:
    """Returns the backup path"""
    return MakeBackups(tarfile_name, filename_path)

def s3_uploader():
    """Returns S3Uploader class"""
    if is_in_testing_mode():
        s3_client = DummyClient('s3_client')
    else:
        s3_client = boto3.client('s3')

    return S3Uploader(
        s3_client, 
        bucket_name, 
        bucket_path , 
        make_backup().return_backup_path(), 
        lifeclycle_policy
    )

def upload_file():
    """Uploads the given file to S3"""
    s3_uploader().upload()

def create_backup():
    """Creates the backup !"""
    make_backup().create_tar_file()

def delete_backup():
    """Deletes the backup"""
    make_backup().delete_file()

def main():
    """Main function, it performs the backup creation, upload to S3 and delete the backup"""
    create_backup()
    upload_file()
    delete_backup()

if __name__ == "__main__":
    main()