#!/usr/bin/env python3

import aws_cdk as cdk

from simple_aws_cicd_pipeline.simple_aws_cicd_pipeline_stack import SimpleAwsCicdPipelineStack


app = cdk.App()
SimpleAwsCicdPipelineStack(app, "simple-aws-cicd-pipeline")

app.synth()
