from aws_cdk import (
    Stack,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions,
    aws_codebuild as codebuild,
    SecretValue,
)
from constructs import Construct


class SimpleAwsCicdPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source_output = codepipeline.Artifact()
        source_action = codepipeline_actions.GitHubSourceAction(
            action_name="Source",
            owner="EmmanuelELOKA",
            repo="https://github.com/EmmanuelELOKA/simple-aws-ci-cd.git",
            # You'll need to create this secret per the docs
            # https://docs.aws.amazon.com/cdk/api/latest/docs/aws-codepipeline-actions-readme.html#github
            oauth_token=SecretValue.secrets_manager("my-github-token"),
            output=source_output,
        )
        pipeline = codepipeline.Pipeline(
            self,
            "MySimplePipeline",
            stages=[
                codepipeline.StageProps(stage_name="Source", actions=[source_action]),
                codepipeline.StageProps(
                    stage_name="Build",
                    actions=[
                        codepipeline_actions.CodeBuildAction(
                            action_name="Build",
                            # Configure your project here
                            project=codebuild.PipelineProject(self, "MyProject"),
                            input=source_output,
                        )
                    ],
                ),
            ],
        )