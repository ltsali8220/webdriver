
from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.service import Service# type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore

import os
import platform
import time
import csv

# Determine OS and set driver path
os_name = platform.system()
print("Operating System Name:", os_name)

if os_name == 'Windows':
    driver_path = r'C:\Windows\chromedriver.exe'
elif os_name == 'Linux':
    driver_path = r'/home/saliv/chrome_driver/chromedriver'
else:
    print("Running on an unsupported OS. Exiting...")
    exit(1)

service = Service(driver_path)

# Directory for CSV files
directory = os.path.expanduser('~/Devops/Python/webdriver/')

# Initialize counters for progress
total_rows = 0
completed_rows = 0

# Loop through CSV files
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        print(f"Opening file: {filename}")

        with open(filepath, mode='r') as file:
            reader = csv.reader(file)

            # Count the total rows in the file (for progress tracking)
            total_rows += sum(1 for _ in reader)
            file.seek(0)  # Reset file pointer to the beginning

            # Loop through each row in the CSV file
            for row in reader:
                if len(row) < 3:
                    print(f"Skipping incomplete row: {row}")
                    continue

                try:
                    # Set Chrome options
                    chrome_options = Options()
                    chrome_options.add_argument('--ignore-certificate-errors')
                    chrome_options.add_argument('--ignore-ssl-errors')

                    # Initialize the WebDriver
                    driver = webdriver.Chrome(service=service, options=chrome_options)

                    # Open the webpage
                    driver.get('https://forms.office.com/Pages/ResponsePage.aspx?id=FTrTJhyUhUKaF3vGe4xRnMu2oQrmD5RBs-zmMhoIfOBUN1dSQ1I4SjlEVVlaTjhROUhQWlpKMTM5Mi4u')
                    
                    # Wait for the first field to be present
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="question-list"]/div[1]/div[2]/div/span/input'))
                    )

                    # Fill in the form fields
                    driver.find_element("xpath", '//*[@id="question-list"]/div[1]/div[2]/div/span/input').send_keys(row[0])
                    driver.find_element("xpath", '//*[@id="question-list"]/div[2]/div[2]/div/span/input').send_keys(row[1])
                    driver.find_element("xpath", '//*[@id="question-list"]/div[3]/div[2]/div/span/input').send_keys(row[2])

                    # Click radio buttons or checkboxes
                    driver.find_element("xpath", '//*[@id="question-list"]/div[4]/div[2]/div/div/div[3]/div/label/span[1]/input').click()
                    driver.find_element("xpath", '//*[@id="question-list"]/div[5]/div[2]/div/div/div[1]/div/label/span[1]/input').click()
                    driver.find_element("xpath", '//*[@id="question-list"]/div[6]/div[2]/div/div/div[2]/div/label/span[1]/input').click()
                    driver.find_element("xpath", '//*[@id="question-list"]/div[7]/div[2]/div/div/div[2]/div/label/span[1]/input').click()
                    driver.find_element("xpath", '//*[@id="question-list"]/div[8]/div[2]/div/div/div[4]/div/label/span[1]/input').click()
                    driver.find_element("xpath", '//*[@id="question-list"]/div[9]/div[2]/div/div/div[2]/div/label/span[1]/input').click()
                    driver.find_element("xpath", '//*[@id="question-list"]/div[10]/div[2]/div/div/div[2]/div/label/span[1]/input').click()
                    driver.find_element("xpath", '//*[@id="question-list"]/div[11]/div[2]/div/div/div[2]/div/label/span[1]/input').click()
                    driver.find_element("xpath", '//*[@id="question-list"]/div[12]/div[2]/div/div/div[2]/div/label/span[1]/input').click()
                    driver.find_element("xpath", '//*[@id="question-list"]/div[13]/div[2]/div/div/div[2]/div/label/span[1]/input').click()
                   
                    # Submit the form
                    submit_button = driver.find_element(By.XPATH, '//*[@id="form-main-content1"]/div/div/div[2]/div[2]/div/button')
                    submit_button.click()
                    
                    # Wait for a moment before closing
                    time.sleep(2)

                except Exception as e:
                    print(f"An error occurred while processing row {row}: {e}")

                finally:
                    # Close the browser for this iteration
                    driver.quit()
                    time.sleep(2)
                    os.system('clear')
                    completed_rows += 1
                    print(f"Processed row: {row[0]}, {row[1]}, {row[2]}")
                    print(f"\nProcessing complete: {completed_rows}/{total_rows} rows completed successfully.")
