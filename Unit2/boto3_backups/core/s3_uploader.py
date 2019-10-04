import json
from core.local_logging import info, error, warning
from botocore.exceptions import ClientError

class S3Uploader:
    """This class is meant to upload files to S3 with the possibility to add Lifecycles
    Args:
        s3_client: The boto3 S3 client
        bucket_name: The name of the S3 Bucket
        bucket_path: The S3 path where the object will be stored
        filename_path: The path where is located the file to upload
        remove_file: Delete file or not 
        lifecycle_configurations: S3 Lifecycle Rule configurations, more details here: 
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_lifecycle_configuration
    """

    def __init__(
        self,
        s3_client,
        bucket_name: str,
        bucket_path: str,
        filename_path: str,
        lifecycle_configuration: dict = {},
        remove_file = False
    ):
        self.s3_client = s3_client
        self.bucket_name = bucket_name
        self.bucket_path = bucket_path
        self.filename_path = filename_path
        self.lifecycle_configuration = lifecycle_configuration
        self.remove_file = remove_file

    def upload(self):
        self._validate_lifecycle_rule()
        self.set_lifecycle_configuration_policy()
        self.upload_file()

    def _validate_lifecycle_rule(self):
        try:
            if not self.lifecycle_configuration:
                warning("No S3 lifecycle rule passed, probably file won't expire automatically.")
                return
            
            info('Validating S3 lifecycle configuration rule.')
            if 'Rules' not in self.lifecycle_configuration:
                error('No Rules were defined in the configuration file. Please take a look at that.')

            info('Good, lifecycle rule is valid.')
        
        except TypeError:
            error(
                'The lifecycle configuration you have passed is not valid, '
                'please verify it and try again, this could be due a missing string, for more '
                'details please refer directly to AWS Documentation here: '
                'https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_bucket_lifecycle_configuration'
            )
                
        except Exception as ex:
            raise ex

    def upload_file(self):
        """This method upload the given file to an S3 Bucket"""
        info(f"Uploading file {self.filename_path.split('/')[-1]} to {self.bucket_name}/{self.bucket_path}.")
        try:
            # s3_client.upload_file('/Users/damien/envs.var', 'wiki-documentation', 's3_lifecycle_config.json')
            self.s3_client.upload_file(
                self.filename_path, 
                self.bucket_name,
                f"{self.bucket_path}/{self.filename_path.split('/')[-1]}"
            )
            info(f"Awesome. File {self.filename_path.split('/')[-1]} has been uploaded successfully.")
        except ClientError as ex:
            raise ex

    def set_lifecycle_configuration_policy(self):
        info(f'Setting Lifecycle rule in bucket {self.bucket_name}.')
        try:
            self.s3_client.put_bucket_lifecycle_configuration(
                Bucket=self.bucket_name,
                LifecycleConfiguration=self.lifecycle_configuration
            )
            info('Great. Lifecycle has been configured correctly.')
        except Exception as ex:
            raise ex
    
