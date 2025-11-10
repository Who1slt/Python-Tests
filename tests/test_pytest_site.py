import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

class TestSauceDemo:
    
    @pytest.fixture
    def driver(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(2)

        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        yield driver
        driver.quit()
    
    def test_successful_login(self, driver):        
        assert "inventory" in driver.current_url
        assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
    
    def test_add_to_cart(self, driver):
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1"
    
    def test_logout(self, driver):
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        assert driver.current_url == "https://www.saucedemo.com/"