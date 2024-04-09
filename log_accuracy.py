import json
from datetime import datetime
import os
import random


def log_accuracy(file_path, accuracies):
    # Check if the file exists
    if os.path.exists(file_path):
        # File exists, load the existing data
        with open(file_path, "r+") as file:
            try:
                file_data = json.load(file)
                # Assuming the file contains a list of records
                if not isinstance(file_data, list):
                    file_data = []
            except json.JSONDecodeError:
                # In case the JSON is empty or corrupted, start a new list
                file_data = []
    else:
        # File doesn't exist, start a new list
        file_data = []

    # Append new accuracy records
    for accuracy in accuracies:
        data = {
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "accuracy": accuracy
        }
        file_data.append(data)

    # Write the updated data back to the file
    with open(file_path, "w") as file:
        json.dump(file_data, file, indent=4)


def generate_accuracies(n=100):
    # Generate n random accuracy values between 0.0 and 1.0
    return [round(random.uniform(0.0, 1.0), 4) for _ in range(n)]


# Example usage
accuracies = generate_accuracies(100)  # Generate 100 random accuracy values
log_accuracy("data.json", accuracies)
