import boto3
aws_resource= boto3.resource("s3")
bucket= aws_resource.Bucket("totaltech")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration ={
        'LocationConstraint':'us-east-2'
    },
    
)

print(response)