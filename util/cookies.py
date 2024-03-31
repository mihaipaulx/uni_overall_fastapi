from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def accept_cookies(driver):
  try:
    # Wait for the accept button to be clickable
    accept_button = WebDriverWait(driver, 0).until(
      EC.element_to_be_clickable(
                (By.XPATH, "//button[" + " or ".join([f"contains(text(), '{text}')" for text in accept_texts]) + "]")
            )
    )
    accept_button.click()
  except:
    pass

accept_texts = ['Accept', 'Agree', 'Save', 'Godkänn']


