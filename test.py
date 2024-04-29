from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path to chromedriver
service = Service(executable_path='C:\\Users\\koval\\PycharmProjects\\python-selenium\\chromedriver.exe')

# Setup WebDriver
driver = webdriver.Chrome(service=service)
driver.get("http://the-internet.herokuapp.com/exit_intent")

try:
    # Wait for the header to be visible
    wait = WebDriverWait(driver, 10)
    header_element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h3')))

    # Execute JavaScript to mimic the mouse moving towards the browser's top (simulating an exit intent)
    driver.execute_script("window.scrollTo(0, -100);")

    # Wait to see if modal appears
    time.sleep(10)

    # Optionally, take a screenshot and save it in the 'screenshots' folder
    driver.save_screenshot('C:\\Users\\koval\\PycharmProjects\\python-selenium\\screenshots\\exit_intent_modal.png')

finally:
    # Close the browser
    driver.quit()
