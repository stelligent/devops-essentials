# AWS Elastic Beanstalk
AWS Elastic Beanstalk Examples. 

# Overview
This repo is a demonstration of Continuous Delivery of a static website to Elastic Beanstalk via CodePipeline, CodeCommit, CodeBuild, and Elastic Beanstalk. Ensure you've configured the [Prerequisites](https://github.com/stelligent/devops-essentials/wiki/Prerequisites) before launching the stack below.

# Upload html.zip file

1. Download [html.zip](https://github.com/stelligent/devops-essentials/blob/master/samples/beanstalk/html.zip) from GitHub
1. Create a new S3 bucket and make note of the unique bucketname name you created

# Launch Stack



# Configure Solution

## Before Launching the Stack

[![Launch CFN stack](https://s3.amazonaws.com/www.devopsessentialsaws.com/img/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#cstack=sn%7Edevops-essentials-beanstalk%7Cturl%7Ehttps://s3.amazonaws.com/www.devopsessentialsaws.com/samples/beanstalk/pipeline.yml)
1. When launching the stack, enter the name of the S3 Bucket you created in the `S3Bucket` CloudFormation parameter

## After Launching the Stack
1. Once the CloudFormation stack is successful, select the checkbox next to the stack and click the **Outputs** tab. 
1. From Outputs, click on the **PipelineUrl** output. The Source action will be in a failed state.
1. From the CodePipeline Source action, click on the CodeCommit provider and copy the **git clone** statement provided by CodeCommit
1. Paste the command in your Terminal
1. From [this](../beanstalk) folder, copy all of its *contents* to your locally cloned Git repo
1. From your Terminal, type `git add .`
1. From your Terminal, type `git commit -am "add new files"`
1. From your Terminal, type `git push`
1. Go back to your pipeline in CodePipeline and see the changes flow through the pipeline
1. Once the pipeline is complete, go to your CloudFormation Outputs and click on the **SiteUrl** Output

# Resources

1. The CloudFormation template is available [here](https://s3.amazonaws.com/www.devopsessentialsaws.com/samples/beanstalk/pipeline.yml).
1. A list of available Elastic Beanstalk templates are available [here](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html#concepts.platforms.nodejs) or from the [CLI](http://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/list-available-solution-stacks.html#examples)





