# Use a stable Debian version (e.g., buster)
FROM python:3.9-buster

# Update the package repository
RUN apt-get update -y

# Install NTP (apt-get install ntp) for time synchronization and restart the ntp (service ntp restart)
RUN apt-get install -y ntp

# Install OpenJDK 11
RUN apt-get install -y openjdk-11-jdk

# Install Spark 3.5.1
RUN curl -O https://downloads.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz && \
  tar -xvf spark-3.5.1-bin-hadoop3.tgz && \
  mv spark-3.5.1-bin-hadoop3 /spark && \
  rm spark-3.5.1-bin-hadoop3.tgz

# Install Hadoop AWS library and AWS Java SDK for S3 support
RUN curl -O https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.2.2/hadoop-aws-3.2.2.jar && \
  mv hadoop-aws-3.2.2.jar /spark/jars/ && \
  curl -O https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.12.702/aws-java-sdk-1.12.702.jar && \
  mv aws-java-sdk-1.12.702.jar /spark/jars/

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV SPARK_HOME=/spark
ENV PATH=$PATH:$SPARK_HOME/bin

# Set working directory
WORKDIR /app

# Copy your PySpark script and any other files required
COPY main.py /app
COPY simple_storage_service.py /app
# COPY data.csv /app
COPY .env /app/.env
COPY requirements.txt /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# When you start the container, it will open a shell prompt and then, you can manually run the Spark job inside the container by: spark-submit main.py
CMD ["/bin/bash"]
