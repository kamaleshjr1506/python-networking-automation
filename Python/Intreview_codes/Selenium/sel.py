from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
driver.maximize_window()
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.ID,"twotabsearchtextbox")))
time.sleep(20)
links = driver.find_elements(By.TAG_NAME,"a")
print("links",len(links))
dropdown

