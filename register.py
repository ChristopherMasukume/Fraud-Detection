model_path = r"C:\Fraud_Detection\model.pkl"

from azureml.core import Workspace, Model

# Connect to the Azure ML workspace
ws = Workspace.from_config()

# Register the model
model = Model.register(
    model_path=model_path,  # Use raw string literal for the file path
    model_name="fraud_detection_model",  # Your model name
    workspace=ws
)
