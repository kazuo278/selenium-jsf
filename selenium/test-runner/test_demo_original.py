# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDemo():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://chrome:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_demo(self):
    self.driver.get("http://localhost:8080/selenium-demo/")
    self.driver.set_window_size(579, 705)
    self.driver.find_element(By.ID, "add-new-item").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1)").text == "品名を入力してください"
    assert self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2)").text == "個数を入力してください"
    self.driver.find_element(By.ID, "new-item-name").click()
    self.driver.find_element(By.ID, "new-item-name").send_keys("ぶどう")
    self.driver.find_element(By.ID, "new-item-amount").send_keys("-1")
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    self.driver.find_element(By.ID, "add-new-item").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "li").text == "個数は1以上の整数を指定してください"
    self.driver.find_element(By.ID, "new-item-amount").click()
    self.driver.find_element(By.ID, "new-item-amount").send_keys("0")
    self.driver.find_element(By.ID, "new-item-amount").click()
    self.driver.find_element(By.ID, "new-item-amount").send_keys("1")
    self.driver.find_element(By.ID, "new-item-amount").click()
    self.driver.find_element(By.ID, "add-new-item").click()
    assert self.driver.find_element(By.ID, "item-table:2:tabel-item-").text == "ぶどう"
    assert self.driver.find_element(By.ID, "item-table:2:table-item-").text == "1"
  
