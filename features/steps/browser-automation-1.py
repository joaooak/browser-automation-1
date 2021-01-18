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
    return

@given('que loguei no site')
def step_impl(context):
    context.driver.find_element_by_id("txtUsername").send_keys("opensourcecms")
    context.driver.find_element_by_id("txtPassword").send_keys("opensourcecms")
    context.driver.find_element_by_id("btnLogin").click()
    return