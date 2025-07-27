from selenium import webdriver
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from login.login import EbayLogin
from Functions.allitems import select_item
import random
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ( # type: ignore
    StaleElementReferenceException,
    TimeoutException,
    ElementClickInterceptedException
)



def main():
  # 1. intialization of web driver
  options = webdriver.ChromeOptions()
  options.add_argument("--log-level=3")
  options.add_argument("--window-size=1200,800") 
  #options.add_argument("--start-fullscreen")
  options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_experimental_option('useAutomationExtension', False)
  driver = webdriver.Chrome(options=options)

  # login in to ebay:
  login_handler= EbayLogin(driver)
  load_dotenv()
  username=os.getenv("USER_NAME")
  password=os.getenv("PASSWORD") 
  login_handler.login(username,password)
  url= os.getenv("URL")
  time.sleep(random.uniform(2, 3))

  #finding store
  driver.get(url)
  time.sleep(random.uniform(2, 3))
  
  wait = WebDriverWait(driver, 10)
  while True:
    try:
        
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "str-loading-spinner__mask")))
        select_item(driver,url)
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Go to next search page']")))
        time.sleep(2)  
        next_button.click()
        time.sleep(3)  

    except TimeoutException:
        print("No more pages or 'Next' button not found.")
        break

    except ElementClickInterceptedException:
        print("Click intercepted. Retrying after delay...")
        time.sleep(2)
        continue

    except StaleElementReferenceException:
        print("Stale element. Retrying...")
        continue
  
  time.sleep(10)
  driver.quit()
  #




if __name__=="__main__":
  main()

