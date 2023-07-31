from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient
#from azure.identity import DefaultAzureCredential
from flask import Flask
app = Flask(__name__)
@app.route("/")
def MyFun():
    #return "Hello, World!"
    keyvault_url = "https://sharesource-vault-1700.vault.azure.net/"
    credential = ManagedIdentityCredential()
    secret_client = SecretClient(vault_url=keyvault_url,credential=credential)
    secret_name = "MyNewSecret"
    secret = secret_client.get_secret(secret_name)
    return secret.value