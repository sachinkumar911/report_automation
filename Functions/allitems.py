from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import time
import random

def select_item(driver,url):
  # finding store
  driver.get(url)
  time.sleep(random.uniform(2, 3))
  # finding item
  section_item= driver.find_elements(By.XPATH,"//section[@class='str-items-grid__container']/article")
  
   
  for item in section_item:
        time.sleep(1)
        
        div= item.find_element(By.CLASS_NAME,'str-item-card__signals-container')
        driver.execute_script("""const rect = arguments[0].getBoundingClientRect();window.scrollBy({ top: rect.top - window.innerHeight / 2, behavior: 'smooth' });""", div)

        time.sleep(2)
        
        button = div.find_element(By.CSS_SELECTOR, "span.menu-button.str-item-card__overflow-button > button")
        time.sleep(1)
        # smooth_scroll_to_element(driver,button)
        
        button.click()
        time.sleep(1)

        div2 = div.find_element(By.CSS_SELECTOR, "span.menu-button.str-item-card__overflow-button > span")
        time.sleep(2)
        div2.click()
        time.sleep(2)
        
        #submit report button
        submit_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Submit report']")))
        submit_button.click()

        time.sleep(3)
        #reason for 
        modal_container = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='ifhReasonForReport']")))
        driver.execute_script("arguments[0].click();", modal_container)
        not_allowed= WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Item not allowed']")))
        driver.execute_script("arguments[0].click();", not_allowed)
        time.sleep(3)

        #detailed reason
        detailed_reason= WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@id='ifhDetailedReason']")))
        driver.execute_script("arguments[0].click();", detailed_reason)
        time.sleep(3)

        adult=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Adult item or content']")))
        driver.execute_script("arguments[0].click();", adult)
        time.sleep(3)

        #discription
        discription=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='ifhReportIssueDescription']")))
        discription.send_keys("Adult Only content not allowed on eBay. Revealing and suggestive sexual content. Explicit & implied nudity and adult themes. Sexual poses with exposed or outlines of genitalia")
        
        time.sleep(3)
        # check point
        check=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//input[@id='ifhReportConfirm']")))
        driver.execute_script("arguments[0].click();", check)
        
        time.sleep(3)
        #final submit
        final_submit= WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Submit report']")))
        driver.execute_script("arguments[0].click();", final_submit)
        
        time.sleep(3)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='ifhOverlayClose']")))
        driver.execute_script("arguments[0].click();", element)

        

         
        
        
        

        

    
    
    
  