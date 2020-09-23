import boto3

file_NUMBER = 2

# Let's use Amazon S3
s3 = boto3.resource('s3')

for i in range(file_NUMBER):
    # Upload a new file
    data = open('json_example'+str(i)+'.json', 'rb')
    s3.Bucket('yangjson').put_object(Key='json_example'+str(i)+'.json', Body=data)