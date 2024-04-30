from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_exit_intent():
    # Setup Chrome WebDriver
    driver = webdriver.Chrome()  # Make sure to use the correct WebDriver for your browser
    driver.set_window_size(1024, 768)  # Set browser window size
    try:
        # Navigate to the target webpage
        driver.get("http://the-internet.herokuapp.com/exit_intent")
        # Simulate the mouse leaving the viewport using JavaScript
        driver.execute_script("window.dispatchEvent(new MouseEvent('mouseout', {'bubbles': true}));")
        time.sleep(2)  # Allow time for the modal to trigger
        # Wait for the modal to appear and check its visibility
        modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "ouibounce-modal"))
        )
        assert modal.is_displayed(), "The modal did not appear"

        print("Test Passed: Exit intent modal is visible.")
        # Take a screenshot when modal is visible
        driver.save_screenshot('exit_intent_modal_visible.png')
        print("Test Passed: Exit intent modal is visible and screenshot taken.")

    except Exception as e:
        print(f"Test Failed: {e}")
        # Take a screenshot on failure
        driver.save_screenshot('test.png')

    finally:
        driver.quit()
test_exit_intent()
