# Use a stable Debian version (e.g., buster)
FROM python:3.9-buster

# Update the package repository
RUN apt-get update -y

# Install OpenJDK 11
RUN apt-get install -y openjdk-11-jdk

# Install Spark 3.5.1
RUN curl -O https://downloads.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz && \
  tar -xvf spark-3.5.1-bin-hadoop3.tgz && \
  mv spark-3.5.1-bin-hadoop3 /spark && \
  rm spark-3.5.1-bin-hadoop3.tgz

# # Install latest PySpark
# RUN pip install pyspark

# Set environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV SPARK_HOME=/spark
ENV PATH=$PATH:$SPARK_HOME/bin

# Set working directory
WORKDIR /app

# Copy your PySpark script and any other files required
COPY main.py /app
COPY data.csv /app
COPY .env /app/.env
COPY requirements.txt /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# When you start the container, it will open a shell prompt and then, you can manually run the Spark job inside the container by: spark-submit main.py
CMD ["/bin/bash"]
