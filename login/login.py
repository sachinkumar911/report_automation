from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    WebDriverException,
)

class EbayLogin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def login(self, username, password):
        try:

            self.driver.get("https://www.ebay.com/signin/")
            time.sleep(random.uniform(2, 3))
            #  Username
            username_input = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='userid']")))
            username_input.send_keys(username)
            time.sleep(random.uniform(3, 5))

            cont_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='signin-continue-btn']")))
            time.sleep(random.uniform(3, 4))
            cont_btn.click()
            #   Password
            password_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='pass']")))
            time.sleep(random.uniform(2, 3))
            password_input.send_keys(password)
            #signin button 
            signin_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='sgnBt']")))
            time.sleep(random.uniform(3, 5))
            signin_btn.click()

        except TimeoutException as e:
            print.error("Timeout while waiting for an element: %s", e)
        except NoSuchElementException as e:
            print.error("Could not find an element: %s", e)
        except ElementClickInterceptedException as e:
            print.error("Element not clickable: %s", e)
        except WebDriverException as e:
            print.error("WebDriver exception occurred: %s", e)
        except Exception as e:
            print.exception("Unexpected error during login: %s", e)
        
