# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the rest of the application code to the container
COPY . /app

# Expose the port your Flask app will listen on
EXPOSE 5000

# Define the command to run your app when the container starts
CMD ["python", "chat3.py"]
