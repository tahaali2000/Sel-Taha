import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR, "body > app-root > app-navbar > div > nav > ul > li:nth-child(2) > a").click()
driver.maximize_window()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "#navbarResponsive > ul").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR, "input[id='country']").send_keys("ind")
countries= driver.find_elements(By.XPATH, "//div[@class='suggestions']/ul/li/a")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/app-root/app-shop/div/app-checkout/div/div[2]/ul[2]/li/a")))

driver.find_element(By.XPATH,"/html/body/app-root/app-shop/div/app-checkout/div/div[2]/ul[2]/li/a").click()
# for country in countries:
#     if country.text == "India":
#         time.sleep(7)
#         country.click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
success= driver.find_element(By.XPATH, "/html/body/app-root/app-shop/div/app-checkout/div[2]/div")
try:
    assert "Success" in success.text
    print("Assertion passed")
except AssertionError:
    print("Assertion failed")
print(success.text)
input("Press enter to continue...")


driver.close()
