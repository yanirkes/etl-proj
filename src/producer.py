import pika
import time
import requests
import configparser

config = configparser.ConfigParser()
config.read('utils/config.ini')

class Producer():
    # responsible for sending messages to queues, making data available for consumers to retrieve and process.

    def __init__(self):
        self.connection = None
        self.channel = None
        self.retry_delay = int(config['general']['retry_delay'])
        self.num_retries = 0

    def connect(self):
        """
        Connect the Producer to the server and open a channel to produce messages.
        """

        try:
            connection_parameters = pika.ConnectionParameters(config['WEB settings']['rabbit_url'], port=config['WEB settings']['rabbit_port'])
            self.connection = pika.BlockingConnection(connection_parameters)
            print("Producer successfully connected")

            self.channel = self.connection.channel()
            self.channel.queue_declare(queue='eventbox')

        except Exception as e:
            # Handle other exceptions, including connection errors
            print(f"Error publishing message: {e}")
            if self.connection.is_open:
                self.connection.close()


    def get_messages(self):
        """
        Establish API calls to the application server for retrieving an event's
         existence, and if no message is found, initiate multiple retries before
          eventually raising an error.
        :return:
        """

        try:
            while(True):

                # Create an API and get a response.
                response = requests.get(config['WEB settings']['app_url'])

                if response.status_code == 200:
                    if "no events found" in response.text:

                        # Retry mechanism
                        print(f"No events found.\nAttempting number {self.num_retries} Retrying in {self.retry_delay} seconds...")
                        self.try_a_retry()
                        time.sleep(self.retry_delay)  # Wait for the specified delay before retrying
                        continue  # Retry the request

                    elif 'Event' in response.text:
                        return response.text
                    else:
                        return ''
                else:
                    return ''

        except requests.exceptions.RequestException as e:
            print('Request error:', e)

    def produce(self):
        """
        Produce a message to initiate a queue. Run as long as getting an error.
        """

        messageId = 1
        while(True):

            message = self.get_messages()
            if message != '' and message is not None:
                print(f"Event {message}, messageId: {messageId}")
                # Produces a message and insert it to the queue.
                self.channel.basic_publish(exchange='', routing_key='eventbox', body=message)

                messageId += 1

        self.connection.close()

    def try_a_retry(self):
        """
        The retry mechanism, for every call it will verify the current number of retries
        and raise an error when the capacity is over.
        """

        if self.num_retries == int(config['general']['num_retries']):
            self.connection.close()
            raise ("No more events in Cloudtrail, and retries capacity is over")
        self.num_retries +=1
