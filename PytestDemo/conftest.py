import pytest


@pytest.fixture
def browser():
    print("🚀 Launching browser")
    driver = webdriver.Chrome()  # Make sure chromedriver is installed
    driver.maximize_window()
    yield driver
    print("🧹 Closing browser")
    driver.quit()