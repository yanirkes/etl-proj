# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR OrcaProj

# Copy the requirements.txt to a temp file
COPY ./requirements.txt /tmp/

# Install the requirements
RUN pip install --requirement /tmp/requirements.txt

# Copy the current directory app and service into the container at /my_app
COPY  . /my_app

# Make port 4000 available to the world outside this container
EXPOSE 4000

# Run your Flask app when the container launches
CMD ["python", "./my_app/ingestion_service_app_opt.py"]