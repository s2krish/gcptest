# Import the Secret Manager client library.
import json
from google.cloud import secretmanager
from gcp.config import credentials

# GCP project in which to store secrets in Secret Manager.
# project_id = "YOUR_PROJECT_ID"

# ID of the secret to create.

project_id = 'truckbase-348717'
secret_id = "testsecret"

# Create the Secret Manager client.
client = secretmanager.SecretManagerServiceClient()
# client = secretmanager.SecretManagerServiceClient(credentials=credentials)

# Build the parent name from the project.
parent = f"projects/{project_id}"

# Create the parent secret.
# secret = client.create_secret(
#     request={
#         "parent": parent,
#         "secret_id": secret_id,
#         "secret": {"replication": {"automatic": {}}},
#     }
# )

# Add the secret version.
# version = client.add_secret_version(
#     request={"parent": secret.name, "payload": {"data": b"hello world!"}}
# )

# Access the secret version.

parent = client.secret_path(project_id, secret_id)

# List all secret versions.
# for version in client.list_secret_versions(request={"parent": parent, "filter": "state:ENABLED"}):
#     # state = response.state.name
#     # print("Got secret version {} with state {}".format(response.name, state))

#     if version.state.name == 'DISABLED': continue

#     response = client.access_secret_version(request={"name": version.name})
#     # state = response.state.name
#     # print("Got secret version {} with state {}".format(response.name, state))
#     # print (dir(response
#     # ))

#     payload = json.loads(response.payload.data.decode("UTF-8"))
#     print (type(payload))
#     print(f"Plaintext: {payload}")

name = f'projects/{project_id}/secrets/{secret_id}/versions/latest'
request = secretmanager.AccessSecretVersionRequest(name=name)
# parent = client.secret_path(project_id, secret_id, 'latest')
# projects/509366951010/secrets/testsecret/versions/1
response = client.access_secret_version(request=request)
# state = response.state.name
# print("Got secret version {} with state {}".format(response.name, state))
# print (dir(response
# ))

payload = json.loads(response.payload.data.decode("UTF-8"))
print (type(payload))
print(f"Plaintext: {payload}")


# name = client.secret_path(project_id, secret_id)

# # response = client.access_secret_version(request={"name": version.name})
# # response = client.get_secret(request={"name": name})
# response = client.get_secret_version(request={"name": name})

# state = response.state.name
# print("Got secret version {} with state {}".format(response.name, state))

# print (dir(response))

#
# WARNING: Do not print the secret in a production environment - this
# snippet is showing how to access the secret material.
# payload = response.payload.data.decode("UTF-8")
# print("Plaintext: {}".format(payload))