from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import os
import platform

os_name = platform.system()
print("Operating System Name:", os_name)

if os_name == 'Windows':
    # Windows-specific code
    print("Running on Windows")
    # Specify the path to chromedriver.exe
    driver_path = r'C:\Windows\chromedriver.exe'
elif os_name == 'Linux':
    # Linux-specific code
    print("Running on Linux")
    # Specify the path to chromedriver
    driver_path = r'/home/saliv/chrome_driver/chromedriver'
else:
    # Other OS-specific code
    print("Running on an unsupported OS")
    # Specify the path to chromedriver
    #   

service = Service(driver_path)


# Set Chrome options
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Initialize the Chrome WebDriver with the Service object and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a webpage
driver.get('https://www.google.com')

# Keep the browser open
input("Press Enter to close the browser...")





# Close the browser
driver.quit()

