import boto3
import argparse
aws_access_key_id=
aws_secret_access_key=
aws_session_token='IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDEwSGoMTudxrRLXMQGaadSCaomvCcBRU6e5Mef/Gya3AIgBnl8x6Enfm9KvmPCBPdEhlDLD59h7EVv+YHbAhrngNMqsAIIcxAAGgw5OTIzODI1MTU4MTgiDNh+lnzbtKWpD9x0QyqNAtEv0G7ArCvW9uK7KpzUakoampsaa8321GBYX3XB/Xk4XXH5bHKgK/yIzwlytEySgDhs3wze1XOHyvmCtJwv3nz34AoVbIsVhVAnbLqyctHXGiYFplrFLTnDIo7YwpdVexVNSYpzSQYJppPD5laEuvZEBWDbXEFlyVMaMlPiSH+2zoZP6z6u1dyW2J8dPvuKEcwBFwM8Bz7i6S/5Vop7OvOEQKuyxgxDj7JZlj9C+pudtHkrfbWw0IMFJ2v/4vooVYhQzGNhfg/vYPmYr2QKzOTkkLF2H957/6SDIotjHPlcCf/wxV0szzRyDdKBvZmuBulpd6gEbmsxsfNYN17Fe12w52Sxf230cXJIwgfHMJGOnrEGOp0BgBxfWNQ2+DJpO6yQMvn78wvRu02bCDHoSZl0Bw1K+Om7kjnJ3FRhM0OHxypbtnZV+fSeGSw34I4l0QDMW//Iprhe0HBJSzp+ze5RfUVofuSZv86Q2eISgp/MX/gATjx4hxs0KG//yuKNUsp/Hhc8P+d1Igj37PtedSBZ9m4ghWEi7UyjXMHfBDKu2SbbEX6bpQTH3XoaR0k4+YOnUw=='

def count_extensions_usage(aws_s3_client, bucket_name):
    extension_usage = {}
    response = aws_s3_client.list_objects(Bucket=bucket_name)
    for obj in response['Contents']:
        file_name = obj['Key']
        file_extension = '.' + file_name.split('.')[-1] if '.' in file_name else ''
        file_size = obj['Size'] / (1024 * 1024)  # Size in MB
        if file_extension not in extension_usage:
            extension_usage[file_extension] = {'count': 0, 'size': 0.0}
        extension_usage[file_extension]['count'] += 1
        extension_usage[file_extension]['size'] += file_size

    for extension, usage in extension_usage.items():
        print(f'{extension}: {usage["count"]} files, usage: {usage["size"]:.2f} MB')

parser = argparse.ArgumentParser(description='Count the usage of each file extension in an S3 bucket.')
parser.add_argument('bucket_name', type=str, help='The name of the S3 bucket.')

args = parser.parse_args()

s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token)


bucket_name = args.bucket_name
count_extensions_usage(s3_client, bucket_name)
