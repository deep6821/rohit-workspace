FROM apache/spark-py:v3.3.1

# Copy the .env file into the container
COPY .env /app/.env

# Set the working directory
WORKDIR /app

# Copy the requirements file
USER root
COPY requirements.txt .
USER $NB_UID

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application configs and code
COPY configs/ /app/configs/
COPY schema/ /app/schema/
COPY src /app/src

# Set environment variables
ENV SPARK_HOME=/opt/spark
ENV PYTHONPATH="/app/src:${PYTHONPATH}"

# Use ENTRYPOINT to specify the command at runtime
ENTRYPOINT ["spark-submit", "--packages=org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1,org.apache.hadoop:hadoop-aws:3.3.4"]

# Specify the PySpark script as the main application
CMD ["src/pipelines/main.py", "--driver-memory=4g", "--executor-memory=4g"]
