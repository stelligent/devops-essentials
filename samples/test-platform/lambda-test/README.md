# Serverless Alexa Example
Example of deploying a Lambda function used by an Alexa skill. For more details on this solution, see [Use AWS CodePipeline to deploy Amazon Alexa skill](https://stelligent.com/2017/07/25/use-aws-codepipeline-to-deploy-amazon-alexa-skill/
). 

The solution is derived from https://github.com/alexa/skill-sample-nodejs-fact/ and AWS serverless deployment examples (particularly the [AWS CodeStar](https://aws.amazon.com/codestar/) for Alexa project template).

# Overview
This repo is a demonstration of Continuous Delivery of an Alexa skill via CodePipeline, CodeCommit, CodeBuild, and CloudFormation. Ensure you've configured the [Prerequisites](https://github.com/stelligent/devops-essentials/wiki/Prerequisites) before launching the stack below.

# Launch Stack

[![Launch CFN stack](https://s3.amazonaws.com/www.devopsessentialsaws.com/img/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#cstack=sn%7Edevops-essentials-alexa%7Cturl%7Ehttps://s3.amazonaws.com/www.devopsessentialsaws.com/samples/serverless/alexa/pipeline-alexa.yml)

# Configure Solution

1. Once the CloudFormation stack is successful, select the checkbox next to the stack and click the **Outputs** tab. 
1. From Outputs, click on the **PipelineUrl** output. The Source action will be in a failed state.
1. From the CodePipeline Source action, click on the CodeCommit provider and copy the **git clone** statement provided by CodeCommit
1. Paste the command in your Terminal
1. From [this](../serverless/alexa) folder, copy **all files** to your locally cloned Git repo
1. From your Terminal, go to the directory of your locally cloned Git repo and type `git add .`
1. From your Terminal (and from the same locally-cloned Git repo directory), type `git commit -am "add new files"`
1. From your Terminal (and from the same locally-cloned Git repo directory), type `git push`
1. Go back to your pipeline in CodePipeline and see the changes flow through the pipeline
1. Once the pipeline is complete, follow the **Configure and Test Alexa Skill** section at [Use AWS CodePipeline to deploy Amazon Alexa skill](https://stelligent.com/2017/07/25/use-aws-codepipeline-to-deploy-amazon-alexa-skill/
).


# Resources

1. The CloudFormation template is available [here](https://s3.amazonaws.com/www.devopsessentialsaws.com/samples/serverless/alexa/pipeline.yml).
