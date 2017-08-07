import json
import boto3
import uuid
import random

cp = boto3.client("codepipeline")
cf = boto3.client("cloudformation")

def lambda_handler(event, context):
    print json.dumps(event, sort_keys=True, indent=4, separators=(',', ': '))

    job_id = event["job_id"] 
    api_url = event["api_url"]

    ########################################################
    # RUN INTEGRATION TESTS AGAINST API ENDPOINT (api_url) #
    ########################################################

    if random.random() < .8:
        _complete_job(job_id)
    else:
        _fail_job(job_id, 'Random test failure')
    return 

def _complete_job(job_id):
    print("Random complete")
    cp.put_job_success_result(jobId=job_id)

def _fail_job(job_id, failure_reason):
    print("Random failure")
    cp.put_job_failure_result(
            jobId=job_id,
            failureDetails={
                'type': 'JobFailed',
                'message': failure_reason,
                'externalExecutionId': uuid.uuid4().hex
            }
        )
