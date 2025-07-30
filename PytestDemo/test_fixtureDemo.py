import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# ---------- Fixture ----------
@pytest.fixture
def browser():
    print("🚀 Launching browser")
    driver = webdriver.Chrome()  # Make sure chromedriver is installed
    driver.maximize_window()
    yield driver
    print("🧹 Closing browser")
    driver.quit()

# ---------- Test using the fixture ----------
def test_google_title(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title

def test_search_input_exists(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    assert search_box.is_displayed()
