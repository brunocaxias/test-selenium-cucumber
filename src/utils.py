from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def click_btn(driver, xpath, timeout=5):
    botao = driver.find_element(By.XPATH, xpath)
    wait = WebDriverWait(driver, timeout=timeout)
    wait.until(lambda x : botao.is_displayed())
    botao.click()
    
def input_text(driver, xpath, text, timeout=5):
    input = driver.find_element(By.XPATH, xpath)
    wait = WebDriverWait(driver, timeout=timeout)
    wait.until(lambda x : input.is_displayed())
    input.send_keys(text)