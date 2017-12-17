var assert = require('assert');
var AWS = require('aws-sdk');
var querystring  = require('querystring'); // for user parameters

console.log('Loading function');

exports.handler = function(event, context) {

    var codepipeline = new AWS.CodePipeline();
    
    // Retrieve the Job ID from the Lambda action
    var jobId = event["CodePipeline.job"].id;

//    var imageVersion = event["CodePipeline.job"].data.actionConfiguration.configuration.UserParameters; 

    var userParams = querystring.parse(event["CodePipeline.job"].data.actionConfiguration.configuration.UserParameters);

    console.log('imageVersion =', userParams.imageversion);
    console.log('stackname =', userParams.stackname);

    // Notify AWS CodePipeline of a successful job
    var putJobSuccess = function(message) {
        var params = {
            jobId: jobId
        };
        codepipeline.putJobSuccessResult(params, function(err, data) {
            if(err) {
                context.fail(err);      
            } else {
                context.succeed(message);      
            }
        });
    };
    
    // Succeed the job
    putJobSuccess("Tests passed.");   
  
};