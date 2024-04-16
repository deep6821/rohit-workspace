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

# When you start the container, it will open a shell prompt and then, you can manually run the Spark job inside the container by: spark-submit main.py
CMD ["/bin/bash"]