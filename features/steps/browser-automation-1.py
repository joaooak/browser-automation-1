#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from behave import *
import time

#driver = webdriver.Chrome("D://Workspace//Browser Automation//browser-automation-1//chromedriver.exe")


##### Steps

@given('que acessei o site OrangeHRM')
def step_impl(context):
    context.driver.get("https://s2.demo.opensourcecms.com/orangehrm/symfony/web/index.php/")

@given('que loguei no site')
def step_impl(context):
    context.stdout = True
    for row in context.table:
        print(str(row))
        print(str(context.table))
    print("oi")
    context.driver.find_element_by_id("txtUsername").send_keys("opensourcecms")
    context.driver.find_element_by_id("txtPassword").send_keys("opensourcecms")
    context.driver.find_element_by_id("btnLogin").click()


'''
@given('que entrei no site "OrangeHRM"')
def AbreSite(driver):
    driver.maximize_window()
    driver.get("https://s2.demo.opensourcecms.com/orangehrm/symfony/web/index.php/")

def FazLogin(driver):
    # Login
    time.sleep(2)
    driver.find_element_by_id("txtUsername").send_keys("opensourcecms")
    driver.find_element_by_id("txtPassword").send_keys("opensourcecms")
    driver.find_element_by_id("btnLogin").click()

    return

def FazPesquisa(driver):
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="empsearch_employee_name_empName"]').send_keys("Danilo")
    driver.find_element_by_name("empsearch_id").send_keys("123")
    driver.find_element_by_name("empsearch_termination").send_keys("Past Employees Only")
    driver.find_element_by_name("empsearch_supervisor_name").send_keys("Zé")
    time.sleep(2)
    driver.find_element_by_name("searchBtn").click()
'''