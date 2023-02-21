# prefect-dbt-k8s-snowflake
Demonstrates how to:
- manage codependent data flows in Prefect Core
- extract & load data to Snowflake
- transform data using dbt
- dockerize the project
- deploy the project to a Kubernetes cluster on AWS
- orchestrate all steps using Prefect Cloud.

	ACCOUNT_ID=`aws sts get-caller-identity --query Account --output text`

	docker build -t prefect-dbt-k8s-snowflake .

	aws ecr create-repository --repository-name prefect-dbt-k8s-snowflake --image-scanning-configuration scanOnPush=true
	aws ecr get-login-password | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com
	docker tag prefect-dbt-k8s-snowflake:latest $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/prefect-dbt-k8s-snowflake:latest
	docker push $ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/prefect-dbt-k8s-snowflake:latest
	prefect register --project jaffle_shop -p flows/

	prefect agent kubernetes install -k YOUR_API_KEY --rbac --label prod
	kubectl apply -f k8s_agent.yaml
