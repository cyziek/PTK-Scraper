import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def selenim_auth(url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_options.add_argument("headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    cookies_button = driver.find_element(By.ID, 'hs-eu-confirmation-button')
    cookies_button.click()
    try:
        captcha_button = driver.find_element(By.ID, "form-recaptcha-submit")
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable((captcha_button)))
        captcha_button.click()
    except:
        print("No captcha button!")

    time.sleep(1)
    driver.quit()
