### Data Engineering
We ingest events from our Kafka cluster and store them in our Data Lake on S3. 
Events are sorted by arriving date. For example `events/recipe_changes/2019/11/29`.
During events processing we heavily rely on execution day to make sure we pick proper chunks of data and keep historical results.

We use Apache Spark to work with data and store it on S3 in parquet format. Our primary programming language is Python.


## Task 1
Using Apache Spark and Python, read the source data, pre-process it and persist (write) it to ensure optimal structure and performance for further processing.  
The source events are located on the `input` folder. 

## Task 2
Using Apache Spark and Python read the processed dataset from Task 1 and: 
1. Extract only recipes that have `beef` as one of the ingredients.
2. Calculate average cooking time duration per difficulty level.
3. Persist dataset as CSV to the `output` folder.  
  The dataset should have 2 columns: `difficulty,avg_total_cooking_time`.

Total cooking time duration can be calculated by formula:
```bash
total_cook_time = cookTime + prepTime
```  
Hint: times represent durations in ISO format.

Criteria for levels based on total cook time duration:
- easy - less than 30 mins
- medium - between 30 and 60 mins
- hard - more than 60 mins.


# Recipe ETL Pipeline
This project implements an ETL (Extract, Transform, Load) pipeline for processing recipe data. The pipeline is designed to read raw recipe data from a Kafka stream, perform data validation and preprocessing, and store the processed data in an S3 bucket. Additionally, it calculates the average total cooking time for recipes containing beef, grouped by difficulty level, and writes the result to another S3 bucket in CSV format.

## Key features
**Preserving Historical Data**:<br>The pipeline ensures that new data is appended to the existing partitions in the S3 bucket, without overwriting the previous records. This is achieved by:
   - Retrieving the latest processed date from the partitioned S3 location.
   - Filtering the incoming data to only include new events that have arrived since the last run.

   <br>This approach allows the pipeline to maintain the complete historical data, enabling accurate analysis and reporting over time.

**Incremental Processing**:<br>The pipeline implements an incremental processing mechanism, where it only processes the new or updated data, rather than reprocessing the entire dataset on each run. This is accomplished by:
   - Retrieving the latest processed date from the partitioned S3 location.
   - Filtering the incoming data to only include new events that have arrived since the last run.

   <br>This optimization improves the efficiency of the pipeline, reducing the processing time and resource usage.

**Partitioning**:<br>The pipeline implements an incremental processing mechanism, where it only processes the new or updated data, rather than reprocessing the entire dataset on each run. This is accomplished by:
   - Efficient data organization and management, allowing for faster queries and analyses.
   - Easier maintenance and troubleshooting, as data can be quickly located by the relevant time periods.
   - Support for incremental processing, as new data can be appended to the appropriate partitions.

   <br>The combination of these features ensures that the ETL pipeline is robust, efficient, and scalable, capable of handling large volumes of recipe data and providing valuable insights.

## Directory Structure
The project follows the following directory structure:
```commandline
|-- Dockerfile
|-- ETL_README.md
|-- README.md
|-- configs
|   `-- dev
|       |-- aws_config.yml
|       |-- kafka_config.yml
|       |-- logging_config.yml
|       `-- spark_config.yml
|-- data
|   |-- input
|   |   |-- recipes-000.json
|   |   |-- recipes-001.json
|   |   `-- recipes-002.json
|   `-- output
|-- docker-compose.yml
|-- requirements.txt
|-- schema
|   `-- schemas.yml
|-- spark.env
`-- src
    |-- __init__.py
    |-- airflow
    |   |-- __init__.py
    |   `-- data_workflow.py
    |-- pipelines
    |   |-- __init__.py
    |   |-- dataload.py
    |   |-- main.py # entry point for the application
    |   `-- prepare.py
    |-- tests
    |   |-- __init__.py
    |   |-- airflow
    |   |   `-- __init__.py
    |   |-- pipelines
    |   |   |-- __init__.py
    |   |   |-- test_dataload.py
    |   |   `-- test_prepare.py
    |   `-- utility
    |       `-- __init__.py
    `-- utility
        |-- __init__.py
        |-- kafka_consumer.py
        |-- kafka_producer.py
        |-- schema.py
        |-- spark_session.py
        `-- utils.py
```

## Pipeline Overview
The ETL pipeline consists of the following main components:

1. **Data Ingestion (Task 1)**: Raw recipe data is ingested from a Kafka stream using the `pipelines.dataload.process_data` function. The ingested data is validated against a predefined schema and written the data(historical and incremental data) to an S3 bucket in Parquet format, partitioned by year, month, and day.

2. **Data Preprocessing (Task 2)**: The preprocessed data from the S3 bucket is read using the `pipelines.prepare.preprocess_data` function. This function extracts recipes containing "beef" as an ingredient, calculates the average total cooking time per difficulty level, and writes the result to another S3 bucket in CSV format.

3. **Airflow Orchestration**: The ETL pipeline is orchestrated using Apache Airflow. <br>The `src.airflow.data_workflow.py` script defines an Airflow DAG (Directed Acyclic Graph) with two tasks: `dataload` and `prepare`. <br> The `dataload` task invokes the `process_data` function, while the `prepare` task invokes the `preprocess_data` function.

## Configuration
The project uses YAML files for configuration. The `configs/dev` directory contains the following configuration files:
- `aws_config.yml`: AWS configuration settings, including access keys, regions, and S3 bucket paths.
- `kafka_config.yml`: Kafka configuration settings, such as bootstrap servers, topics, and serialization options.
- `logging_config.yml`: Logging configuration settings, including log levels, formats, and CloudWatch integration.
- `spark_config.yml`: Spark configuration settings, such as app name, executor memory, and shuffle partitions.

## Dependencies
The project dependencies are listed in the `requirements.txt` file.<br>You can install them using the following command:  
`pip install -r requirements.txt`

## Docker Compose
The project includes a `docker-compose.yml` file for running the pipeline components (Spark, Kafka, Zookeeper, and Airflow) using Docker containers. You can start the pipeline by running: <br>
`docker build -t hf-pyspark-app .`
`docker-compose up -d`

## CI/CD
The project includes a GitHub Actions workflow (`.github/workflows/recipe-etl-cicd.yml`) for Continuous Integration and Continuous Deployment (CI/CD). The workflow performs the following steps:

1. **Lint**: Run pylint for code linting.
2. **Test**: Run pytest for unit testing.
3. **Deploy**: If linting and testing pass, build and run the Docker Compose services, and trigger the Airflow DAG.

## Schema
The `schema/schemas.yml` file defines the input and output schemas for the pipeline. The input schema defines the structure of the raw recipe data, while the output schema defines the structure of the processed data containing average cooking times per difficulty level.

## Tests
The project includes unit tests for the `dataload` and `prepare` modules. The tests are located in the `tests/pipelines` directory.

# High Level Diagram



# Troubleshooting

Here are some potential issues and troubleshooting steps for this production-level application:

1. **Data Quality Issues**:
   - Ensure that the input data is conforming to the expected schema by implementing data quality checks.
   - Handle missing or corrupt data gracefully by implementing appropriate error handling and logging mechanisms.
   - Consider implementing data validation and cleansing steps before ingesting the data into the pipeline.

2. **Performance Issues**:
   - Monitor the application's performance using tools like Spark UI, CloudWatch, or other monitoring solutions.
   - Tune Spark configurations (e.g., executor memory, cores, shuffle partitions) based on the workload and available resources.
   - Optimize the pipeline by identifying and addressing potential bottlenecks, such as inefficient data transformations or skewed data partitioning.
   - Consider implementing caching or persisting intermediate datasets to reduce redundant computations.

3. **Scalability Issues**:
   - Monitor the application's resource usage (CPU, memory, network, etc.) and scale the infrastructure accordingly.
   - Consider using auto-scaling mechanisms to automatically adjust resources based on demand.
   - Implement partitioning and parallelization strategies to distribute the workload across multiple executors or nodes.
   
4. **Dependency Management**:
   - Use a virtual environment or containerization (e.g., Docker) to ensure consistent and isolated dependencies across different environments.
   - Consider using a package manager (e.g., pip, conda) to manage and version dependencies.

5. **Error Handling and Logging**:
   - Implement robust error handling mechanisms to gracefully handle and recover from failures.
   - Use centralized logging solutions (e.g., CloudWatch Logs) to aggregate and analyze logs from different components of the application.
   - Set up alerts and notifications for critical errors or failures.

6. **Configuration Management**:
   - Store configurations in a centralized and version-controlled repository (e.g., Git) for better management and traceability.
   - Consider using a dedicated configuration management tool (e.g., AWS Systems Manager Parameter Store, Consul) for storing and retrieving configurations securely.
   - Implement environment-specific configurations (e.g., development, staging, production) to ensure consistent behavior across different environments.

7. **Scheduling and Monitoring**:
   - Use a scheduling tool (e.g., Apache Airflow, AWS Step Functions) to orchestrate and monitor the periodic execution of the pipeline.
   - Set up monitoring and alerting mechanisms to track the pipeline's health, progress, and potential issues.

8. **Data Retention and Backup**:
   - Implement a data retention policy to manage the lifecycle of the input, processed, and output data.
   - Set up regular backups of the data and configurations to ensure recoverability in case of failures or disasters.
9. **Security and Access Control**:
   - Implement appropriate security measures, such as encryption, access control, and authentication mechanisms, to protect sensitive data and configurations.
   - Review and regularly update security best practices and configurations to mitigate potential vulnerabilities.

10. **Documentation and Knowledge Sharing**:
    - Maintain comprehensive documentation for the application, including architecture diagrams, component descriptions, and operational procedures.
    - Encourage knowledge sharing within the team and organization to ensure smooth maintenance and future enhancements.
