import pika
import json
from src.anomally_detection_service import anomalyDetectionService
import configparser

config = configparser.ConfigParser()
config.read('utils/config.ini')

class Consumer():
    # A consumer in RabbitMQ retrieves and processes messages from queues,
    # performing the specified actions or services associated with those messages.

    def __init__(self, dbs_obj):
        self.dbs_obj = dbs_obj
        self.tag = None
        self.connection = None

    def connect(self):
        """
        Connect the consumer to the server and open a channel to consume messages.
        """

        try:
            connection_parameters = pika.ConnectionParameters(config['WEB settings']['rabbit_url'], port=config['WEB settings']['rabbit_port'])
            self.connection = pika.BlockingConnection(connection_parameters)
            print("Consumer successfully connected")

            self.channel = self.connection.channel()
            self.channel.queue_declare(queue='eventbox')

            # If set than the msg would be consumed in any free consumer. Otherwise it will persist the order by consumer.
            self.channel.basic_qos(prefetch_count=1)
            self.tag = self.channel.basic_consume(queue='eventbox', on_message_callback= self.on_message_received)

            print("starting consuming")
            self.channel.start_consuming()

        except Exception as e:
            # Handle other exceptions, including connection errors
            print(f"Error publishing message: {e}")
            if self.connection.is_open:
                self.connection.close()

    def on_message_received(self, ch, method, properties,body):

        """
        Used in consumer applications, is a callback that gets executed when a message is received from a queue

        :param ch: It represents the channel on which the message was received.
        :param method:  the message delivery method.
        :param properties: message attributes such as headers, content type, and etc.
        :param body: the actual message content or payload.
        """
        print(f"\nConsumer {self.tag} received request")

        body_json = json.loads(body.decode().replace("'", '"'))
        self.process_event(body_json)
        ch.basic_ack(delivery_tag=method.delivery_tag)

        print("Finished processing the message\n")
    
    def process_event(self,event):
        """
        The process event get a message and active the anomaly detection service, which
        is part of the consumer to do.
        :param event: The event that should be processed.
        """
        anomalyDetectionService().detect_anomaly(event, self.dbs_obj)
