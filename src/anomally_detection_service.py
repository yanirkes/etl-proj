from pymongo import MongoClient
from src.anomally_detection_model import AnomalyDetector
from pymongo.errors import ConnectionFailure
import configparser

config = configparser.ConfigParser()
config.read('utils/config.ini')


class MongoDbServer:
    # This class role is to create a connection to MongoDB, read and write data.

    def __init__(self):
        self.connect()
        self.collection = None
        self.db = None

    def connect(self):
        try:
            db_url = config['Database']['db_url']
            client = MongoClient(db_url)
            self.db = client[config['Database']['db']]
            self.collection = self.db[config['Database']['collection']]

        except ConnectionFailure as e1:
            # Handle the connection failure gracefully, e.g., log the error or exit the application
            print(f"Failed to connect to MongoDB: {e1}")

        except Exception as e2:
            # Handle other exceptions, if necessary
            print(f"An unexpected error occurred: {e2}")

    def select(self, key, event):
        """
        Read data from the database using a key, and event.
        :param key: Key to find the desired row data.
        :param event: The event that contains information on the primary key.
        :return: the MongoDB result.
        """
        if key == '':
            raise ValueError(f"The key - {key}, is empty")

        if event == {}:
            raise ValueError(f"The event is empty")

        return self.collection.find_one({key: event[key]})

    def write_to_db(self, row_data):
        """
        Write to the database.
        :param row_data: the given row data.
        """

        if row_data == '' or row_data is None:
            raise ValueError(f"The given row data is empty")

        self.collection.insert_one(row_data)
        print("Successfully inserted the following row data: ", row_data)


class anomalyDetectionService:
    # This class is responsible for handling the task of identifying irregularities
    # in a given event. It will execute a decision-making process based on the obtained
    # results, such as uses the anomaly detection mechanism, verifies the
    # event's existence in MongoDB, and take a final action.

    @staticmethod
    def detect_anomaly(event, mongo_obj):

        model = AnomalyDetector()
        doc = mongo_obj.select("Event id", event)

        if doc is None:

            # calculates an anomaly score
            anomaly_score = model.calc_anomaly()

            if anomaly_score > 0:
                event.update({"anomaly_score": anomaly_score})
                mongo_obj.write_to_db(event)
                print(f"Event: {event['Event id']} has successfully inserted")

            else:
                print(f"Event: {event['Event id']} failed to detected as an abnormal event")

        else:
            print(f"Event: {doc['Event id']}, already exists in the db, with {doc['anomaly_score']} anomaly score")
