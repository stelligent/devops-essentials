var AWS = require('aws-sdk');
AWS.config.update({region: 'us-east-1'});
console.log('Loading function');

exports.handler = function(event, context) {
    var codepipeline = new AWS.CodePipeline();
    var params = {
          name: 'tleavey-alexa-with-permissions-CodePipelineStack-ANT1CDT8I2JD' /* required */
    };

    codepipeline.startPipelineExecution(params, function(err, data) {
          if (err) console.log(err, err.stack); // an error occurred
          else     console.log(data);           // successful response
    });
};