import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_tutorials_ninja():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    time.sleep(3)
    expected_title="Your Store"
    actual_title=driver.title
    time.sleep(3)
    assert expected_title.__eq__(actual_title)
    time.sleep(3)
    driver.quit()