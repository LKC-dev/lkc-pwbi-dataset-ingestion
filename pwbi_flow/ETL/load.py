import json
import time
from datetime import datetime
from io import StringIO
from urllib.parse import quote_plus
import boto3

def push_datalake(name, data):
    data.to_csv(name, encoding="utf8", index=False)
    bucket = 'XXXXXXX' #REPLACE WITH YOURS 
    csv_buffer = StringIO()
    data.to_csv(csv_buffer, encoding="utf8", index=False)
    s3_resource = boto3.resource('s3',
                                aws_access_key_id= 'XXXXXXX' #REPLACE WITH YOURS
                                aws_secret_access_key= 'XXXXXXX' #REPLACE WITH YOURS
    s3_resource.Object(bucket, 
                       'pwbi/'+ str(time.strftime('%Y/%m/%d/')) + name).put(Body=csv_buffer.getvalue())
    print("Data uploaded sucessfuly in S3 -> " + name)
    print(time.ctime())
