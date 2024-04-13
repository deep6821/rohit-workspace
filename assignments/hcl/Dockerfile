# # Use an official Python runtime as a parent image
# FROM python:3.8-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install Java and download Apache Spark
# RUN apt-get update && apt-get install -y default-jre
# RUN wget -q https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
# RUN tar -xvzf spark-3.1.2-bin-hadoop3.2.tgz

# # Set environment variables
# ENV SPARK_HOME=/app/spark-3.1.2-bin-hadoop3.2
# ENV PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH

# # Install PySpark
# RUN pip install pyspark

# # Copy the CSV file into the container
# COPY data.csv /app
# COPY main.py /app

# # Run your PySpark script
# CMD ["spark-submit", "main.py"]

# Use the official Apache Spark PySpark image as a parent image
FROM apache/spark-py:v3.3.0

# Set the working directory in the container
WORKDIR /app

# Copy your PySpark script and any other files required
COPY main.py /app
COPY data.csv /app

# Set the environment variable to point to the Spark bin directory
ENV PATH="${SPARK_HOME}/bin:${PATH}"

# When you start the container, it will automatically execute the Spark job specified in main.py
# CMD ["spark-submit", "--master", "local[*]", "main.py"]

# Run a long-lived process in the foreground to keep the container running
# CMD ["tail", "-f", "/dev/null"]

# When you start the container, it will open a shell prompt and then, you can manually run the Spark job inside the container by: spark-submit main.py
CMD ["/bin/bash"]