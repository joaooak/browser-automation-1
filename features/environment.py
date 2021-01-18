#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

##### Antes de alguma ação

def before_all(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()

def before_step(context, step):
    time.sleep(2)
