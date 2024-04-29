from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to chromedriver
service = Service(executable_path='C:\\Users\\koval\\PycharmProjects\\python-selenium\\chromedriver.exe')

# Setup WebDriver
driver = webdriver.Chrome(service=service)
driver.get("http://the-internet.herokuapp.com/exit_intent")

try:
    # Execute JavaScript to trigger exit intent modal
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_tag_name('h3'))

    # Wait for modal to appear
    modal = driver.find_element_by_id('myModal')

    # Optionally, take a screenshot and save it
    driver.save_screenshot('C:\\Users\\koval\\PycharmProjects\\python-selenium\\screenshots\\exit_intent_modal.png')

finally:
    # Close the browser
    driver.quit()
