# Data Processing Application

This README provides instructions on how to run the data processing application, both directly using Python and using Docker.

## Prerequisites

- Python 3.9 or later installed on your system (for direct Python execution)
- Docker installed on your system (for running in a container)

## Running the Application Directly with Python
If you want to run the application directly without Docker, follow these steps:

1. Ensure you're in the directory containing the Python files.

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the main data processing script:
   ```bash
   python data_processor.py
   ```
4. Run the tests:
   ```bash
   python -m pytest test_data_processor.py
   ```

## Running the Application with Docker

To build the Docker image, run the following command in the directory containing the Dockerfile:

```bash
docker build -t data-processing-app .
```

## Running the Docker Container
You have two options for running the container:
# Option 1: Run the container without automatic removal
If you prefer a simpler command and don't need the container to be removed automatically:
```bash
docker run -it data-processing-app:latest
```

# Option 2: Run and automatically remove the container
This option ensures the container is removed after it stops and assigns a specific name to your container:

```bash
docker run -it --rm --name data-processor-container data-processing-app
```

## Basic Docker Commands
```bash
List all Docker images: docker images
List all Docker containers (including stopped ones): docker ps -a
Stop a running container: docker stop <container_id>
Start a stopped container: docker start <container_id>
Open a bash shell in a running container: docker exec -it <container_id> /bin/bash
```
Replace <container_id> with the actual ID or name of your container.

## Troubleshooting
If you encounter any issues, ensure that:

1. The Dockerfile is in the same directory as your application files.
2. You have the necessary permissions to run Docker commands.
3. The Docker daemon is running on your system.
