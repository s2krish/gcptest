from pathlib import Path

GCP_SERVICE_ACCOUNT_CRENDENTIAL_FILE = f"{Path(__file__).resolve().parent.parent}/gcptest.json"

print (GCP_SERVICE_ACCOUNT_CRENDENTIAL_FILE)

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(GCP_SERVICE_ACCOUNT_CRENDENTIAL_FILE)