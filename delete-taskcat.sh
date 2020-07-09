#!/bin/bash
# sudo chmod +x *.sh
# ./delete-TASKCAT_CODE.sh 

AWS_REGION=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone | sed 's/\(.*\)[a-z]/\1/')
PREFIX=tCaT
# Name used in .taskcat.yml
PROJECT_NAME=deoa

# Generated Code by TASKCAT_CODE. For example: 7806754vf2r1494aa8b64d1av821418881
TASKCAT_CODE=${1:-TBD}  
# Generated App Code for Nested Stacks. For example: 2G44LSVW82291
NESTED_APP_CODE=${2:-TBD}

echo Environment: $TASKCAT_CODE

echo "Removing buckets previously used by this script"
aws s3api list-buckets --query 'Buckets[?starts_with(Name, `tcat-deoa`) == `true`].[Name]' --output text | xargs -I {} aws s3 rb s3://{} --force

echo "Deleting $PROJECT_NAME stacks"

# Declare an array of string with type
declare -a StringArray=("beanstalk" "static")
 
# Iterate the string array using for loop
for val in ${StringArray[@]}; do
   echo $val
   echo "Deleting $PREFIX-$PROJECT_NAME-$val-$TASKCAT_CODE"
   aws cloudformation delete-stack --stack-name $PREFIX-$PROJECT_NAME-$val-$TASKCAT_CODE
   aws cloudformation wait stack-delete-complete --stack-name $PREFIX-$PROJECT_NAME-$val-$TASKCAT_CODE
done