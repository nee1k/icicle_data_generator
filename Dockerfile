# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script into the container at /usr/src/app
COPY log_accuracy.py .

# Install any needed dependencies
# (Assuming you don't have external dependencies, this step is optional)
# RUN pip install --no-cache-dir -r requirements.txt

# Run log_accuracy.py when the container launches
CMD ["python", "log_accuracy.py"]