import json
import traceback
import requests
import time
import logging
from gcp.config import credentials
from google.cloud import pubsub_v1

import sys

logger = logging.getLogger('django')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('subscriber - %(asctime)s [%(levelname)s] %(message)s - %(filename)s:%(lineno)d')
handler.setFormatter(formatter)
logger.addHandler(handler)

project_id = 'truckbase-348717'
topic = f'projects/{project_id}/topics/test-pubsub-topic10'
subscription_id = 'test-pubsub-topic10-sub1'

# subscriber = pubsub_v1.SubscriberClient(credentials=credentials)
subscriber = pubsub_v1.SubscriberClient()  # from environment variable GOOGLE_APPLICATION_CREDENTIALS

subscription_path = subscriber.subscription_path(project_id, subscription_id)


logger = logging.getLogger('django')

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    # if message:
    # print ("message")
    # print (dir(message))
    # print (message.attributes)

    j_data = json.loads(message.data.decode('utf-8'))
    j_data['pubsub_id'] = message.message_id
    # print(f"Received {j_data}.")
    r = requests.post("http://127.0.0.1:8000/", json=j_data)
    logger.info("Response")
    logger.info(message.message_id)
    logger.info(r.text)

    if r.status_code in (200, 201):
        time.sleep(10)
        logger.info("ack")
        message.ack()

flow_control = pubsub_v1.types.FlowControl(max_messages=10)
# streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback, flow_control=flow_control)

logger.info(f"Listening for messages on {subscription_path}..\n")

# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber:
    try:
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        # streaming_pull_future.result(timeout=timeout)
        streaming_pull_future.result()
    except Exception as e:
        logger.info(f"Pubsub pull failed. {e}")
        logger.info(traceback.format_exc())
        streaming_pull_future.cancel()  # Trigger the shutdown.
        streaming_pull_future.result()  # Block until the shutdown is complete.