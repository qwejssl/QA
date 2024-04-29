from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def setup_driver():
    """Setup and return a Chrome WebDriver with specified window size."""
    driver = webdriver.Chrome()  # Ensure the correct WebDriver path is set or WebDriver is in PATH
    driver.set_window_size(1024, 768)
    return driver

def navigate_to_page(driver, url):
    """Navigate the WebDriver to a specified URL."""
    driver.get(url)

def simulate_mouse_exit(driver):
    """Simulate the mouse leaving the viewport to trigger the exit intent modal."""
    driver.execute_script("window.dispatchEvent(new MouseEvent('mouseout', {'bubbles': true}));")
    time.sleep(2)  # Wait for modal to potentially trigger

def verify_modal_displayed(driver):
    """Wait for the exit intent modal to appear and verify its visibility."""
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "ouibounce-modal"))
    )
    assert modal.is_displayed(), "The modal did not appear"

def take_screenshot(driver, filename):
    """Take a screenshot and save it to a specified filename."""
    driver.save_screenshot(filename)

def test_exit_intent():
    """Test the visibility of the exit intent modal on the page."""
    driver = setup_driver()
    try:
        navigate_to_page(driver, "http://the-internet.herokuapp.com/exit_intent")
        simulate_mouse_exit(driver)
        verify_modal_displayed(driver)
        take_screenshot(driver, 'exit_intent_modal_visible.png')
        print("Test Passed: Exit intent modal is visible and screenshot taken.")
    except Exception as e:
        print(f"Test Failed: {e}")
        take_screenshot(driver, 'test_failure.png')
    finally:
        driver.quit()

# Run the test function
test_exit_intent()
