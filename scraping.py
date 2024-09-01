from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

# Set up Chrome options and service
options = Options()

# Set the download directory to the current working directory
download_directory = os.getcwd()

# Configure Chrome to use the specified download directory
prefs = {
    "download.default_directory": download_directory,  # Set default download directory
    "download.prompt_for_download": False,  # Do not prompt for download location
    "directory_upgrade": True,  # Enable directory upgrades
    "safebrowsing.enabled": True  # Enable safe browsing
}
options.add_experimental_option("prefs", prefs)

# Allow insecure content and ignore certificate errors
options.add_argument("--allow-running-insecure-content")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-web-security")

# Initialize the WebDriver with the configured options
service = Service(executable_path='C:/Users/Syrin/Downloads/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

# Load the website
driver.get("http://xteam.xbio.top/CellMarker/index.jsp")

# Wait for the page to load completely
time.sleep(3)

# Open the text file and read lines
with open("cluster14.txt", "r") as file:
    lines = file.readlines()

# Iterate over each line in the text file
for i, line in enumerate(lines):
    gene_name = line.strip()

    # Click on the text area with id "quickSearchInfo"
    search_box = driver.find_element(By.ID, "quickSearchInfo")
    search_box.clear()  # Clear any existing text
    search_box.send_keys(gene_name)  # Paste the text from the current line

    # Click the button with class "btn btn-default"
    search_button = driver.find_element(By.CLASS_NAME, "btn.btn-default")
    search_button.click()

    # Wait for 3 seconds for the new page to load
    time.sleep(3)

    # Try to find the Excel download button
    try:
        excel_button = driver.find_element(By.CLASS_NAME, "dt-button.buttons-excel.buttons-html5")
    except:
        excel_button = None

    # Scroll only if the button is not found
    if excel_button is None:
        # Scroll down to find the Excel download button
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)  # Wait for scrolling to complete
        try:
            excel_button = driver.find_element(By.CLASS_NAME, "dt-button.buttons-excel.buttons-html5")
        except:
            print(f"Excel button not found for {gene_name}")
            continue  # Skip to the next iteration if the button is not found

    # Click on the Excel download button
    excel_button.click()

    # Wait for the download to complete (you might need to adjust the sleep time depending on your network speed)
    time.sleep(5)

    # Rename the downloaded file to the gene name
    original_filename = max([download_directory + "/" + f for f in os.listdir(download_directory)], key=os.path.getctime)
    new_filename = os.path.join(download_directory, f"{gene_name}.xlsx")
    os.rename(original_filename, new_filename)

    # Optionally, navigate back to the main page for the next iteration
    driver.back()
    time.sleep(2)

# Close the driver
driver.quit()




