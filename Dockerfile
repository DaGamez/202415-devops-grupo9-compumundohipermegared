#docker rmi -f post-management-image; docker build -t post-management-image . 
#docker rm -f post-management-container ;
# docker run -p 8000:8000 --name post-management-container -e DB_USER=postgres -e DB_PASSWORD=postgres -e DB_PORT=5432 -e DB_NAME=post_db -e DB_HOST=post-db -e USERS_PATH=http://users_app:3000 post-management-image 

# Use the official Python image from the Docker Hub
FROM python:3.9-slim


# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app/ .

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=main.py

# Run the application with Gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "main:app"]