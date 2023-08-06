# Use the official Python image as the base image
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the project dependencies
RUN pip install -r requirements.txt

# Install Pillow for image handling
RUN pip install Pillow

# Specify the command to run your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
