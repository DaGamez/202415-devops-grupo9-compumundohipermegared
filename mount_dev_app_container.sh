#!/bin/bash
# Mount run Flask app for Linux

# Stop and remove existing containers if they exist
docker stop black_list_local_app
docker rm black_list_local_app

# Create a custom network bridge if it doesn't exist
docker network create --driver bridge black_list_network || true

# Build the Docker image
docker build -t black_list_local_app_image .

# Run the Flask app container
docker run -d --name black_list_local_app \
    --network black_list_network \
    -p 5000:5000 \
    -e DB_USER=postgres \
    -e DB_PASSWORD=postgres \
    -e DB_PORT=5432 \
    -e DB_NAME=postgres \
    -e DB_HOST=black_list_local_db \
    black_list_local_app_image