#!/bin/bash

# Run docker compose for Linux, removing first and then running again in detached mode
docker-compose down --rmi all
docker-compose up --build -d