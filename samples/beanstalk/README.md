# AWS Elastic Beanstalk
AWS Elastic Beanstalk Examples. 

# Overview
This repo is a demonstration of Continuous Delivery of a static website to Elastic Beanstalk via CodePipeline, CodeCommit, CodeBuild, and Elastic Beanstalk. Ensure you've configured the [Prerequisites](https://github.com/stelligent/devops-essentials/wiki/Prerequisites) before launching the stack below.


# Launch Stack

From your [AWS Cloud9](https://github.com/paulduvall/aws-compliance-workshop/wiki/0.2#setup-aws-cloud9) terminal, type the following to setup your directory structure:

```
sudo rm -rf ~/environment/tmp-doea
cd ~/environment
aws s3 mb s3://doea-eb-$(aws sts get-caller-identity --output text --query 'Account')
aws s3 mb s3://doea-eb-sitebucket-$(aws sts get-caller-identity --output text --query 'Account')
git clone https://github.com/PaulDuvall/devops-essentials.git tmp-doea
cd tmp-doea/samples/beanstalk
zip -r doea-eb-samples.zip -x '*.git*'
aws s3 sync ~/environment/tmp-doea/samples/beanstalk/ s3://doea-eb-$(aws sts get-caller-identity --output text --query 'Account')
aws s3 sync ~/environment/tmp-doea/samples/beanstalk s3://doea-eb-sitebucket-$(aws sts get-caller-identity --output text --query 'Account')
```

## Launch the CloudFormation stack from the CLI

From your Cloud9 terminal, type the following:

```
aws cloudformation create-stack --stack-name doea-beanstalk --capabilities CAPABILITY_NAMED_IAM --disable-rollback --template-body file:///home/ec2-user/environment/tmp-doea/samples/beanstalk/pipeline.yml --parameters ParameterKey=EmailAddress,ParameterValue=fake-email@fake-fake-fake-email.com ParameterKey=CodeCommitS3Bucket,ParameterValue=doea-eb-$(aws sts get-caller-identity --output text --query 'Account') ParameterKey=CodeCommitS3Key,ParameterValue=doea-eb-samples.zip ParameterKey=S3Bucket,ParameterValue=doea-eb-sitebucket-$(aws sts get-caller-identity --output text --query 'Account')
```


## After Launching the Stack
1. Once the CloudFormation stack is successful, select the checkbox next to the stack and click the **Outputs** tab. 
1. From Outputs, click on the **PipelineUrl** output. The Source action will be in a failed state.
1. Once the pipeline is complete, go to your CloudFormation Outputs and click on the **SiteUrl** Output

# Resources

1. The CloudFormation template is available [here](https://s3.amazonaws.com/www.devopsessentialsaws.com/samples/beanstalk/pipeline.yml).
1. A list of available Elastic Beanstalk templates are available [here](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html#concepts.platforms.nodejs) or from the [CLI](http://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/list-available-solution-stacks.html#examples)





