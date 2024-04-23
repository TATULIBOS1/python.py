
import boto3
import argparse

aws_access_key_id=
aws_secret_access_key=
aws_session_token='IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDEwSGoMTudxrRLXMQGaadSCaomvCcBRU6e5Mef/Gya3AIgBnl8x6Enfm9KvmPCBPdEhlDLD59h7EVv+YHbAhrngNMqsAIIcxAAGgw5OTIzODI1MTU4MTgiDNh+lnzbtKWpD9x0QyqNAtEv0G7ArCvW9uK7KpzUakoampsaa8321GBYX3XB/Xk4XXH5bHKgK/yIzwlytEySgDhs3wze1XOHyvmCtJwv3nz34AoVbIsVhVAnbLqyctHXGiYFplrFLTnDIo7YwpdVexVNSYpzSQYJppPD5laEuvZEBWDbXEFlyVMaMlPiSH+2zoZP6z6u1dyW2J8dPvuKEcwBFwM8Bz7i6S/5Vop7OvOEQKuyxgxDj7JZlj9C+pudtHkrfbWw0IMFJ2v/4vooVYhQzGNhfg/vYPmYr2QKzOTkkLF2H957/6SDIotjHPlcCf/wxV0szzRyDdKBvZmuBulpd6gEbmsxsfNYN17Fe12w52Sxf230cXJIwgfHMJGOnrEGOp0BgBxfWNQ2+DJpO6yQMvn78wvRu02bCDHoSZl0Bw1K+Om7kjnJ3FRhM0OHxypbtnZV+fSeGSw34I4l0QDMW//Iprhe0HBJSzp+ze5RfUVofuSZv86Q2eISgp/MX/gATjx4hxs0KG//yuKNUsp/Hhc8P+d1Igj37PtedSBZ9m4ghWEi7UyjXMHfBDKu2SbbEX6bpQTH3XoaR0k4+YOnUw=='
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token, region_name='us-east-1')

def purge_bucket(aws_s3_client, bucket_name):
    object_keys = []
    for obj in aws_s3_client.list_objects(Bucket=bucket_name)['Contents']:
        object_keys.append(obj['Key'])

    response = aws_s3_client.delete_objects(
        Bucket=bucket_name,
        Delete={
            'Objects': [{'Key': key} for key in object_keys]
        }
    )
    status_code = response['ResponseMetadata']['HTTPStatusCode']
    if status_code == 200:
        print(f'The bucket {bucket_name} has been purged.')
    else:
        print(f'The bucket {bucket_name} has not been purged.')

parser = argparse.ArgumentParser(description='Purge an S3 bucket.')
parser.add_argument('bucket_name', type=str, help='The name of the S3 bucket to purge.')

args = parser.parse_args()

bucket_name = args.bucket_name
purge_bucket(s3_client, bucket_name)


