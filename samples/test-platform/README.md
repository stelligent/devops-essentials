# Test Platform
Test all the other CloudFormation stacks in the [samples](../)

# Setup

The following is typically configured one time per AWS account. The following examples assume AWS region `us-east-1`

1. Create a *Secure String* parameter named `GitHubToken` in [Parameter Store](https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#Parameters:)
1. Modify the [buildspec-test.yml](./buildspec-test.yml) to obtain the values of the parameters you defined in Parameter Store

# Launch Stack

[![Launch CFN stack](https://s3.amazonaws.com/www.devopsessentialsaws.com/img/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#cstack=sn%7Edevops-essentials-test-platform%7Cturl%7Ehttps://s3.amazonaws.com/www.devopsessentialsaws.com/samples/test-platform/pipeline.yml)

# Configure Solution

1. Once the CloudFormation stack is successful, select the checkbox next to the stack and click the <strong>Outputs</strong> tab. 
1. From Outputs, click on the **PipelineUrl** output. The Source action will be in a failed state.
1. From the CodePipeline Source action, click on the CodeCommit provider and copy the **git clone** statement provided by CodeCommit
1. Paste the command in your Terminal
1. From this [samples/test-platform](../test-platform) folder, copy the **[buildspec-test.yml](./buildspec-test.yml)** file to your locally cloned CodeCommit git repo
1. From this [samples/test-platform](../test-platform) folder, copy the **[buildspec.yml](./buildspec.yml)** file to your locally cloned CodeCommit git repo
1. From this [samples/test-platform](../test-platform) folder, copy the **[sam-template.yml](./sam-template.yml)** file to your locally cloned CodeCommit git repo
1. From this [samples/test-platform](../test-platform) folder, copy the **[index.js](./index.js)** file to your locally cloned CodeCommit git repo
1. From your Terminal, type `git add .`
1. From your Terminal, type `git commit -am "add new files"`
1. From your Terminal, type `git push`
1. Go back to your pipeline in CodePipeline and see the changes flow through the pipeline
1. Once the pipeline is complete, go to your CloudFormation stacks to see the CloudFormation stacks being generated

# Resources

1. The CloudFormation template is available [here](https://s3.amazonaws.com/www.devopsessentialsaws.com/samples/test-platform/pipeline.yml).





