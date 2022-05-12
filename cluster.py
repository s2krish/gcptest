from gcp.config import credentials
from google.cloud import container_v1


project_id = 'truckbase-348717'
location = 'us-central1-c'

# client = container_v1.ClusterManagerClient(credentials=credentials)
client = container_v1.ClusterManagerClient() # from environment variable GOOGLE_APPLICATION_CREDENTIALS
# Create a fully qualified location identifier of form `projects/{project_id}/location/{zone}'.
cluster_location = client.common_location_path(project_id, location)
# Create the request object with the location identifier.
request = {"parent": cluster_location}
# list_response = client.list_clusters(request)
# print(
#     f"There were {len(list_response.clusters)} clusters in {location} for project {project_id}."
# )
# for cluster in list_response.clusters:
#     print(f"- {cluster.name}")

name = f'projects/{project_id}/zone/{location}/clusters/testcluster'

cluster = client.get_cluster(name=name)

print (dir(cluster))