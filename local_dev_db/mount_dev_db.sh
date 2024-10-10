#!/bin/bash
# Mount dev database for Linux

# Stop and remove existing container if it exists
docker stop black_list_local_db
docker rm black_list_local_db

# Create a custom network bridge if it doesn't exist
docker network create --driver bridge black_list_network || true

# Build the Docker image
docker build -t black_list_local_db_image .

# Run the container with the custom network
docker run -d --name black_list_local_db \
    --network black_list_network \
    -p 5432:5432 black_list_local_db_image