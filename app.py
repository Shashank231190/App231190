from flask import Flask
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# Initialize the ManagedIdentityCredential
credential = ManagedIdentityCredential()

# Replace 'YOUR_KEYVAULT_NAME' with the name of your Azure Key Vault

vault_url = f"https://sharesource-vault-1700.vault.azure.net/"

# Initialize the SecretClient with the ManagedIdentityCredential
client = SecretClient(vault_url=vault_url, credential=credential)

@app.route('/')
def home():
    # Replace 'YOUR_SECRET_NAME' with the name of the secret you want to retrieve
    secret_name = 'MyNewSecret'

    try:
        # Use the SecretClient to get the secret value
        secret = client.get_secret(secret_name)
        return f"The secret value is: {secret.value}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run()
