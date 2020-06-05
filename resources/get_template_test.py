import boto3

def get_template(sourcebucket,baselinetemplate):
    '''
        Read a template file and return the contents
    '''
    #print("Reading resources from " + templatefile)
    s3 = boto3.resource('s3')
    #obj = s3.Object('cf-to-create-lambda','5-newbaseline.yml')
    obj = s3.Object(sourcebucket,baselinetemplate)
    return obj.get()['Body'].read().decode('utf-8')

print(get_template('account-creation-hands-lab.com','Accountbaseline.yml'))
print(get_template('mpsa-reinvent19','AccountCreationLambda.zip'))
print(get_template('awsmpsa-reinvent-2019','Accountbaseline.yml'))
