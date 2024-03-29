import boto3

from .config import S3_KEY, S3_SECRET, S3_LOCATION

s3 = boto3.client("s3", aws_access_key_id=S3_KEY,
                  aws_secret_access_key=S3_SECRET)


def upload_file_to_s3(file, bucket_name, acl="public-read"):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """

    s3.upload_fileobj(
        file,
        bucket_name,
        file.filename,
        ExtraArgs={
            "ACL": acl,
            "ContentType": file.content_type
        }
    )

    return "{}{}".format(S3_LOCATION, file.filename)
