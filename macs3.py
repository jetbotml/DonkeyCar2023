import uuid
import boto3
import numpy as np
import pandas as pd
from io import StringIO, BytesIO

s3 = boto3.client("s3")
s3_resource = boto3.resource('s3')

mac_address = uuid.getnode()
mac_address_hex = ':'.join(['{:02x}'.format((mac_address >> elements) & 0xff) for elements in range(0,8*6,8)][::-1])
print(mac_address_hex)

S3_mac_address = mac_address_hex.replace(":", "")
print(S3_mac_address)

print("S3 Bucket List")
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])
