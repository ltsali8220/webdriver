from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Specify the path to chromedriver.exe
driver_path = r'C:\Windows\chromedriver.exe'
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

