# AWS Infrastructure and Deployment Pipeline Samples
AWS Infrastructure and Deployment Pipeline Samples

# Launch Stacks
Choose **Deploy to AWS** to launch the template in your account. All solutions use the **us-east-1** region.

Solution | Launch Template | README
------------ | ------------- | -------------
**Static** | [![Launch Static Website Stack with CloudFormation](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?stackName=devops-essentials-static&templateURL=https://s3.amazonaws.com/www.devopsessentialsaws.com/samples/static/pipeline.yml) | [README](./static)
**EC2** | [![Launch EC2 Stack with CloudFormation](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?stackName=devops-essentials-ec2&templateURL=https://s3.amazonaws.com/www.devopsessentialsaws.com/samples/ec2/pipeline.yml) | [README](./ec2)
**OpsWorks** | [![Launch OpsWorks Stack with CloudFormation](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#cstack=sn%7Edevops-essentials-opsworks%7Cturl%7Ehttps://s3.amazonaws.com/www.devopsessentialsaws.com/samples/opsworks/pipeline.yml) | [README](./opsworks)
**Elastic Beanstalk** | [![Launch Elastic Beanstalk Stack with CloudFormation](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#cstack=sn%7Edevops-essentials-beanstalk%7Cturl%7Ehttps://s3.amazonaws.com/www.devopsessentialsaws.com/samples/beanstalk/pipeline.yml) | [README](./beanstalk)
**ECS**  | [![Launch ECS Stack with CloudFormation](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#cstack=sn%7Edevops-essentials-ecs%7Cturl%7Ehttps://s3.amazonaws.com/www.devopsessentialsaws.com/samples/ecs/pipeline.yml) | [README](./ecs)
**Serverless** | [![Launch Serverless Stack with CloudFormation](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#cstack=sn%7Edevops-essentials-serverless%7Cturl%7Ehttps://s3.amazonaws.com/www.devopsessentialsaws.com/samples/serverless/pipeline.yml) | [README](./serverless)
**Alexa** | [![Launch Serverless Stack for Alexa with CloudFormation](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#cstack=sn%7Edevops-essentials-alexa%7Cturl%7Ehttps://s3.amazonaws.com/www.devopsessentialsaws.com/samples/serverless/alexa/pipeline.yml) | [README](./serverless/alexa)

# Changes

1. Go to [Find a Color](http://htmlcolorcodes.com/)
1. In the `css/bootstrap.min.css` within the `html` directories of [samples](https://github.com/stelligent/devops-essentials/tree/master/samples), search for `.bg-primary{color:#fff;background-color:` and update to the hexadecimal color immediately after `background-color:#` 
