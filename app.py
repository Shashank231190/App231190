#from azure.identity import ManagedIdentityCredential
#rom azure.keyvault.secrets import SecretClient
#from azure.identity import DefaultAzureCredential
from flask import Flask
app = Flask(__name__)
@app.route("/")
def MyFun():
    return "Hello, World!"
    #keyvault_name = os.environ.get("AZURE_VAULT_NAME")
    #keyvault_url = "https://" +  keyvault_name + ".vault.azure.net/"
    #credential = DefaultAzureCredential()
    #secret_client = SecretClient(vault_url=keyvault_url,credential=credential)
    #secret_name = "MyNewSecret"
    #secret = secret_client.get_secret(secret_name)
    #print(f"Secret Value: {secret.value}")