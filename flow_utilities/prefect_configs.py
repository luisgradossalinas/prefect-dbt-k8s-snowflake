from prefect.run_configs import KubernetesRun, RunConfig
from prefect.storage.github import GitHub
from prefect.client.secrets import Secret

def set_run_config() -> RunConfig:
    aws_account_id = Secret("AWS_ACCOUNT_ID").get()
    return KubernetesRun(
        labels=["prod"],
        image=f"{aws_account_id}.dkr.ecr.us-east-1.amazonaws.com/prefect-dbt-k8s-snowflake:latest",
    )

def set_storage(flow_name: str) -> GitHub:
    return GitHub(
        repo="luisgradossalinas/prefect-dbt-k8s-snowflake",
        path=f"flows/{flow_name}.py",
        access_token_secret="GITHUB_ACCESS_TOKEN",
    )



