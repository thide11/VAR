import boto3
import os

# Let's use Amazon S3

# session = boto3.Session(profile_name='acesso')
# print(client)
# client.res
# s3 = client.resource('s3')

class S3:
  def __init__(self):
    self.client = boto3.client(
      's3',
      aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
      aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
    )

  bucket = "meet-indexer"

  def get_presigned_url(self, file_path : str):
    print("a")
    return self.client.generate_presigned_url('get_object',
      Params={'Bucket': self.bucket,
              'Key': file_path},
      ExpiresIn=3600
    )
    
  def upload_file(self, file_path : str, s3_path : str):

    # video = open(file_path, 'rb')

    response = self.client.upload_file(
      file_path,
      self.bucket,
      s3_path,
      # ACL="public-read",
      # Key=s3_path,
      # Body=video
    )
    print(response)
    return response != None
  
  def file_exists(self, file_path : str):
    try:
      self.client.get_object(
          Bucket='meet-indexer',
          Key=file_path,
      )
      return True
    except self.client.exceptions.NoSuchKey:
        return False

# for bucket in client.list_buckets()["Buckets"]:
#     print(bucket)