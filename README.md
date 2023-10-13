# Orca security etl project

## Set up the project

Please follow these next steps:

1. Open CMD and navigate to the directory you wish to run the project from. Use `cd` command.
For instance:
`
cd user\py_project\orca_proj
`

2. When you reach the right directories, you can clone the project to it, please run the following command:
`
git clone http://github/yanirkes/etl-proj
`
3. Install local environment:
   * use python or python3, depends on you installation
   * run - python python -m venv venv
   * source venv/bin/activate
   * pip install -r requirements.txt

4. Once you cloned the git repo, make sure you are in the root file (OrcaProj). Then run the docker-compose as follows:
`
docker-compose up
`
Wait until the docker finishes to load all the servers.

5. Please open another terminal (a new window in the CMD), and navigate to the root project (OrcaProj). Then, run the following command:
`
python main.py

`


## Documentation

I am delighted to announce the successful implementation of our project architecture, which harnesses the power of several cutting-edge technologies to create a robust and efficient solution. Below, I'll detail the key technologies we employed and the advantages they bring to our project.

1. Python: 
   I chose Python as the programming language to write the architecture.   
   
2. Flask:
Our project leverages Flask, a lightweight and flexible web framework, to build our web application. Flask simplifies web development with its minimalistic design, enabling us to focus on the specific features we need.
In this case, the task was to read events from Cloudtrail. Assuming Cloudtrail stores all the events in S3, the application only has to read it and return the results. The guidelines for the task was to assume the received 
Cloudtrail events as the following figure, and it wasn't necessary to build infrastructure for connecting AWS clouds.

3. RabbitMQ:
For ingestion and queue management, we integrated RabbitMQ, a robust message broker. RabbitMQ excels in managing communication between distributed components, providing asynchronous processing, and ensuring reliability in data exchange.
In addition, it is easy to implement and handles well a degree of complexity, where it can manage multiple queues, such that each queue can differ by topic (different source) and or by event (content)

4. MongoDB:
MongoDB, a NoSQL database, serves as our project's data store. Its document-based structure offers flexibility and scalability, making it an excellent choice for handling diverse data formats and accommodating future growth.

5. Docker:
Docker containerization enhances our project's portability and deployment efficiency. With Docker, we encapsulate our application, ensuring consistency across different environments and simplifying scaling and management.
Each of these technologies was selected for its unique strengths, resulting in a well-rounded and agile project architecture. Together, they provide a robust foundation for our solution, delivering high performance, scalability, and maintainability. We are excited about the future possibilities and growth potential of our project with this tech stack in place.
