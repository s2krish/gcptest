import json
import datetime
from gcp.config import credentials
from google.cloud import pubsub_v1

project_id = 'truckbase-348717'
topic_id = 'test-pubsub-topic10'


# publisher = pubsub_v1.PublisherClient(credentials=credentials)
publisher = pubsub_v1.PublisherClient()  # from environment variable GOOGLE_APPLICATION_CREDENTIALS
topic_path = publisher.topic_path(project_id, topic_id)


data = {
    'load_assignment_id': 10,
    'time': f'{datetime.datetime.now()}'
}
data_str  = json.dumps(data)

# Data must be a bytestring
data_str = data_str.encode("utf-8")

print (data_str)

future = publisher.publish(topic_path, data_str)

print(future.result())


