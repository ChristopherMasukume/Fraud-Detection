from azureml.core import Workspace, Model, Environment
from azureml.core.model import InferenceConfig
from azureml.core.webservice import AciWebservice, Webservice

# Initialize workspace
ws = Workspace.from_config()

# Load the model
model = Model(ws, name="model.pkl")  # Replace 'your_model_name' with your model's name

# Define the environment (if not using the YAML method)
env = Environment(name="fraud_detection_env")
deps = CondaDependencies.create(pip_packages=["azureml-core", "scikit-learn", "joblib", "numpy"])
env.python.conda_dependencies = deps

# Define inference configuration
inference_config = InferenceConfig(entry_script="score.py", environment=env)

# Define deployment configuration
aci_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

# Deploy the model
service = Model.deploy(workspace=ws,
                       name="fraud-detection-service",
                       models=[model],
                       inference_config=inference_config,
                       deployment_config=aci_config)

service.wait_for_deployment(show_output=True)

print(f"Service deployed at: {service.scoring_uri}")
