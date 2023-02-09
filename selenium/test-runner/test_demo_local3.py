# Generated by Selenium IDE
import pytest
import time
import json
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

class TestDemo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.driver.implicitly_wait(10)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_demo(self):
    self.driver.get("http://localhost:8080/selenium-demo/")
    self.driver.set_window_size(579, 705)
    self.driver.find_element(By.ID, "add-new-item").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1)").text == "品名を入力してください"
    assert self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2)").text == "個数を入力してください"
    self.driver.find_element(By.ID, "new-item-name").click()
    self.driver.find_element(By.ID, "new-item-name").send_keys("ぶどう")
    self.driver.find_element(By.ID, "new-item-amount").send_keys("-1")
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    self.driver.find_element(By.ID, "add-new-item").click()
    time.sleep(1)
    assert self.driver.find_element(By.CSS_SELECTOR, "li").text == "個数は1以上の整数を指定してください"
    self.driver.find_element(By.ID, "new-item-amount").click()
    # 追加：前の入力内容を削除
    self.driver.find_element(By.ID, "new-item-amount").clear()
    self.driver.find_element(By.ID, "new-item-amount").send_keys("1")
    self.driver.find_element(By.ID, "add-new-item").click()
    time.sleep(1)
    assert self.driver.find_element(By.ID, "item-table:2:tabel-item-").text == "ぶどう"
    assert self.driver.find_element(By.ID, "item-table:2:table-item-").text == "1"
