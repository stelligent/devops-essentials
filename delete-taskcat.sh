#!/bin/bash
# sudo chmod +x *.sh
# ./delete-taskcat.sh 

AWS_REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone | sed 's/\(.*\)[a-z]/\1/')

# Generated Code by TaskCat. For example: 7806754vf2r1494aa8b64d1av821418881
TASKCAT=${1:-TBD}  
# Generated App Code for Nested Stacks. For example: 2G44LSVW82291
NESTED_APP_CODE=${2:-TBD}

echo Environment: $TASKCAT

echo "Removing buckets previously used by this script"
aws s3api list-buckets --query 'Buckets[?starts_with(Name, `tcat-ce`) == `true`].[Name]' --output text | xargs -I {} aws s3 rb s3://{} --force

echo "Deleting Lesson 8 stacks"
aws cloudformation delete-stack --stack-name tCaT-ce-l8-$TASKCAT-$AWS_REGION
aws cloudformation wait stack-delete-complete --stack-name tCaT-ce-l8-$TASKCAT-$AWS_REGION
aws cloudformation delete-stack --stack-name tCaT-ce-l8-$TASKCAT

echo "Deleting Lesson 5 stacks"
aws cloudformation delete-stack --stack-name tCaT-ce-l5-rest-ddb-$TASKCAT
aws cloudformation delete-stack --stack-name tCaT-ce-l5-rest-ebs-$TASKCAT
aws cloudformation delete-stack --stack-name tCaT-ce-l5-rest-kms-$TASKCAT
aws cloudformation delete-stack --stack-name tCaT-ce-l5-rest-s3-$TASKCAT

echo "Deleting Lesson 4 stacks"
aws cloudformation delete-stack --stack-name tCaT-ce-l4-$TASKCAT-cloudfront
aws cloudformation wait stack-delete-complete --stack-name tCaT-ce-l4-$TASKCAT-cloudfront
aws cloudformation delete-stack --stack-name tCaT-ce-l4-$TASKCAT-acm
aws cloudformation wait stack-delete-complete --stack-name tCaT-ce-l4-$TASKCAT-acm
aws cloudformation delete-stack --stack-name tCaT-ce-l4-$TASKCAT

echo "Deleting Lesson 3 stacks"
aws cloudformation delete-stack --stack-name tCaT-ce-l3-$TASKCAT-$AWS_REGION-rds
aws cloudformation wait stack-delete-complete --stack-name tCaT-ce-l3-$TASKCAT-$AWS_REGION-rds
aws cloudformation delete-stack --stack-name tCaT-ce-l3-$TASKCAT-$AWS_REGION-NestedApp-$NESTED_APP_CODE
aws cloudformation wait stack-delete-complete --stack-name tCaT-ce-l3-$TASKCAT-$AWS_REGION-NestedApp-$NESTED_APP_CODE
aws cloudformation delete-stack --stack-name tCaT-ce-l3-$TASKCAT-$AWS_REGION
aws cloudformation wait stack-delete-complete --stack-name tCaT-ce-l3-$TASKCAT-$AWS_REGION
aws cloudformation delete-stack --stack-name tCaT-ce-l3-$TASKCAT-$AWS_REGION-vpc
aws cloudformation wait stack-delete-complete --stack-name tCaT-ce-l3-$TASKCAT-$AWS_REGION-vpc
aws cloudformation delete-stack --stack-name tCaT-ce-l3-$TASKCAT

echo "Deleting Lesson 1 stacks"
aws cloudformation delete-stack --stack-name tCaT-ce-lesson1-pipeline-$TASKCAT
aws cloudformation delete-stack --stack-name tCaT-ce-lesson1-automate-$TASKCAT
aws cloudformation delete-stack --stack-name tCaT-ce-lesson1-pipeline-$TASKCAT