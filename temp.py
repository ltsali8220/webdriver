import os
import csv

# Specify the directory containing CSV files
directory = '/home/saliv/Devops/Python/webdriver/'  # Replace with your folder path

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        print(f"Opening file: {filename}")

        # Open and read the CSV file
        with open(filepath, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0])
                # print(row)  # Print each row or process it as needed
                # for user_data in row:
                #     print(user_data[0])