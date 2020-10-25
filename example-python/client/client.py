import boto3
import base64
import json
import io

client = boto3.client('lambda')
v = client.invoke(FunctionName='latex_hello', LogType='Tail')
print(v)
print(base64.b64decode(v['LogResult']).decode('utf-8'))
res = v['Payload'].read()
r = json.loads(res)
pdf = base64.b64decode(r['output'])
with open("hello.pdf", "wb") as f:
    f.write(pdf)
