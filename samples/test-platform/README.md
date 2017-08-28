# Test Platform
1. Tests all the other CloudFormation stacks in the [samples](../)
1. Creates a Lambda function that is AUTOMATICALLY run once a day which creates all the CloudFormation stacks

# !WARNING!
When this pipeline is created (by following all of the directions below), AWS resources will be created once a day due to the automatic Lambda function. If you do not want resources to be made daily, make sure to delete all of these resources when you're finished. At the very least, go into AWS Lambda, look for the function that matches your Cloudformation stack names, and delete the Lambda function, which will stop the pipeline from running every day.

# Setup

The following is typically configured one time per AWS account. The following examples assume AWS region `us-east-1`

1. Create a *Secure String* parameter named `GitHubToken` in [Parameter Store](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Parameters:)
1. Modify the [buildspec-cfnstacks.yml](./buildspec-cfnstacks.yml) to obtain the values of the parameters you defined in Parameter Store

# Launch Stack

[![Launch CFN stack](https://s3.amazonaws.com/www.devopsessentialsaws.com/img/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#cstack=sn%7Edevops-essentials-test-platform%7Cturl%7Ehttps://s3.amazonaws.com/www.devopsessentialsaws.com/samples/test-platform/pipeline.yml)

# Configure Solution

1. Once the CloudFormation stack is successful, select the checkbox next to the stack and click the <strong>Outputs</strong> tab. 
1. From Outputs, click on the **PipelineUrl** output. The Source action will be in a failed state.
1. From the CodePipeline Source action, click on the CodeCommit provider and copy the **git clone** statement provided by CodeCommit
1. Paste the command in your Terminal
1. From this [samples/test-platform](../test-platform) folder, copy the **[buildspec-cfnstacks.yml](./buildspec-cfnstacks.yml)** file to your locally cloned CodeCommit git repo
1. From this [samples/test-platform](../test-platform) folder, copy the **[buildspec-lambda.yml](./buildspec-lambda.yml)** file to your locally cloned CodeCommit git repo
1. From this [samples/test-platform](../test-platform) folder, copy the **[sam-template.yml](./sam-template.yml)** file to your locally cloned CodeCommit git repo
1. From this [samples/test-platform](../test-platform) folder, copy the **[index.js](./index.js)** file to your locally cloned CodeCommit git repo
1. Open your local **[index.js](./index.js)** file and change the variable CHANGE_TO_CODEPIPELINE_NAME to match the name of your CodePipeline pipeline. (The name can be found by going to AWS CodePipeline in the AWS Console.)
1. From your Terminal, type `git add .`
1. From your Terminal, type `git commit -am "add new files"`
1. From your Terminal, type `git push`
1. Go back to your pipeline in CodePipeline and see the changes flow through the pipeline
1. Once the pipeline is complete, go to your CloudFormation stacks to see the CloudFormation stacks being generated

# Resources

1. The CloudFormation template is available [here](https://s3.amazonaws.com/www.devopsessentialsaws.com/samples/test-platform/pipeline.yml).





