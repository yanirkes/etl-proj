# Orca security project

## Documentation

I am delighted to announce the successful implementation of our project architecture, which harnesses the power of several cutting-edge technologies to create a robust and efficient solution. Below, I'll detail the key technologies we employed and the advantages they bring to our project.

1. Python: 
   I chose python as the programming language to write the architecture.   
   
2. Flask:
Our project leverages Flask, a lightweight and flexible web framework, to build our web application. Flask simplifies web development with its minimalistic design, enabling us to focus on the specific features we need.
In this case, the task was to read event from cloudtrail. Assuming cloudtrail stores all the events in S3, the application only has to read it and return the results. The guidelines for the task was to assume the received 
cloudtrail event as the following figure, and it wasn't necessary to build infrastructure for connecting AWS clouds.

3. RabbitMQ:
For ingestion and queue management, we integrated RabbitMQ, a robust message broker. RabbitMQ excels in managing communication between distributed components, providing asynchronous processing, and ensuring reliability in data exchange.
In addition, 

4. MongoDB:
MongoDB, a NoSQL database, serves as our project's data store. Its document-based structure offers flexibility and scalability, making it an excellent choice for handling diverse data formats and accommodating future growth.

5. Docker:
Docker containerization enhances our project's portability and deployment efficiency. With Docker, we encapsulate our application, ensuring consistency across different environments and simplifying scaling and management.
Each of these technologies was selected for its unique strengths, resulting in a well-rounded and agile project architecture. Together, they provide a robust foundation for our solution, delivering high performance, scalability, and maintainability. We are excited about the future possibilities and growth potential of our project with this tech stack in place.