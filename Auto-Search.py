import os
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Path to your video file
video_path = r'C:\Users\vpnzo\OneDrive\Desktop\Python\sample\pic.jpg'

# Open the video file
os.startfile(video_path)

# Wait for the video to finish playing (you can adjust the sleep time as needed)
import time
time.sleep(10)

# Open a new Chrome browser window
driver_service = Service(r'C:\Users\vpnzo\OneDrive\Desktop\Python\chromedriver.exe')
driver_service.start()
driver = webdriver.Remote(driver_service.service_url)

# Perform a Google search
search_query = "HelloWorld"
search_url = "https://www.google.com/search?q=" + search_query
driver.get(search_url)

# Click on the first search result
first_result = driver.find_element(By.CSS_SELECTOR, "div.g a")
first_result.click()

# Close the browser window
driver.quit()
