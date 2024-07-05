# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Install pytest for running tests
RUN pip install --no-cache-dir pytest

# When you start the container, it will open a shell prompt and then, you can manually run the Spark job inside the container by: spark-submit main.py
# CMD ["/bin/bash"]

# Use JSON format for CMD and ensure we're in the correct directory
CMD ["sh", "-c", "cd /app && python -m pytest test_data_processor.py && python data_processor.py"]
