from src import producer
from src import consumer
from src import anomally_detection_service as dbs
import threading as thrd
import configparser

config = configparser.ConfigParser()
config.read('utils/config.ini')


if __name__ == '__main__':
    db_obj = dbs.MongoDbServer()
    db_obj.connect()
    pr_obj = producer.Producer()
    con_obj = consumer.Consumer(db_obj)
    con_obj2 = consumer.Consumer(db_obj)

    pr_obj.connect()

    # Create separate processes for the server and client
    server_process = thrd.Thread(target=pr_obj.produce)
    client_process1 = thrd.Thread(target=con_obj.connect)
    client_process2 = thrd.Thread(target=con_obj2.connect)
    # #
    # Start both processes
    server_process.start()
    client_process1.start()
    client_process2.start()
    #
    # Wait for both processes to finish
    server_process.join()
    client_process1.join()
    client_process2.join()

