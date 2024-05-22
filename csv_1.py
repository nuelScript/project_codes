import csv
import json

# File paths
json_file = 'path_to_your_json_file.json' #'/home/pi/shared_data.json'
csv_file = 'path_to_your_csv_file.csv'    #'/home/pi/data.csv'

# Load JSON data
with open(json_file, 'r') as file:
    data = json.load(file)

# Data extraction for CSV
csv_data = [
    data["today_date"],
    data["num_fruits"],
    data["fruit_type"],
    data["dht22"]["temperature"],
    data["dht22"]["humidity"],
    data["ethanol"]["sensor_value"],
    data["ethylene"]["sensor_value"],
    data["Grade"]
]

# CSV headers
headers = ["Today's Date", "Number of Fruits", "Fruit Type", "Temperature", "Humidity", "Ethanol", "Ethylene", "Grade"]

# Writing to CSV
with open(csv_file, 'a', newline='') as file:  # 'a' is for append mode
    writer = csv.writer(file)
    # Check if the file is empty to write headers
    file.seek(0, 2)  # Move the cursor to the end of the file
    if file.tell() == 0:  # If file is empty, write headers
        writer.writerow(headers)
    writer.writerow(csv_data)

print("Data appended to CSV file successfully.")
