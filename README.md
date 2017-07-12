# DevOps Essentials on AWS
In *DevOps Essentials on AWS Complete Video Course*, you'll learn how to automate the infrastructure and deployment pipelines using AWS services and tools so if you're some type of software or DevOps-focused engineer or architect interested in learning how to use [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/) to create a full-lifecycle software delivery solution, it's the course for you. The focus of the course is on deployment pipeline architectures and its implementations versus software architectures.

# Overview
This repo is a demonstration of Continuous Delivery of a static website to S3 via CodeBuild and CodePipeline. To launch, you'll need to specify a unique S3 bucket name for the website bucket that will be created along with a GitHub token. Review and ensure you've configured the [Prerequisites](http://www.devopsessentialsaws.com/) before launching the stack below.

[![Launch CFN stack](https://s3.amazonaws.com/www.devopsessentialsaws.com/img/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#cstack=sn%7Edevops-essentials-static%7Cturl%7Ehttps://s3.amazonaws.com/www.devopsessentialsaws.com/samples/static/pipeline.yml)

The CloudFormation template is available [here](https://s3.amazonaws.com/www.devopsessentialsaws.com/samples/static/pipeline.yml).

Go to [Samples](https://github.com/stelligent/devops-essentials/tree/master/samples) to launch different DevOps on AWS solutions.

Here's the [course website](http://www.devopsessentialsaws.com/)
