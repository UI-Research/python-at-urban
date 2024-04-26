from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
## NOTE: Some users may want to try a Firefox Driver instead;
## Can comment above two lines and uncomment the below two lines
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
import pandas as pd
import re
import time

def click_button(identifier, driver, by=By.XPATH, timeout=15):   
    '''
    This function waits until a button is clickable and then clicks on it.`

    Inputs:
        identifier (string): The Id, XPath, or other way of identifying the element to be clicked on
        by (By object): How to identify the identifier (Options include By.XPATH, By.ID, By.Name and others).
            Make sure 'by' and 'identifier' correspond to one other as they are used as a tuple pair below.
        timeout (int): How long to wait for the object to be clickable

    Returns:
        None (just clicks on button)
    '''

    element_clickable = EC.element_to_be_clickable((by, identifier))
    element = WebDriverWait(driver, timeout=timeout).until(element_clickable)
    driver.execute_script("arguments[0].click();", element)


def select_dropdown(identifier, driver,  by=By.XPATH, value=None, option=None,  index=None):
    '''
    This function clicks on the correct dropdown option in a dropdown object.
    It first waits until the element becomes selectable before locating the proper drop down menu. Then it selects the proper option.
    If the page doesn't load within 15 seconds, it will return a timeout message.

    Inputs:
        id (string): This is the HTML 'value' of the dropdown menu to be selected, 
            found through inspecting the web page.
        value (string): The value to select from the dropdown menu.
        index (int): If index is not None, function assumes we want to select an option by its index instead of by specific value. 
            In this case, should specify that value = None.
    
    Returns:
        None (just selects the right item in the dropdown menu)
    '''
    element_clickable = EC.element_to_be_clickable((by, identifier))
    element = WebDriverWait(driver, timeout=15).until(element_clickable)
    if value is not None:
        Select(element).select_by_value(value)
    elif option is not None: 
        Select(element).select_by_visible_text(option)
    else:
        Select(element).select_by_index(index)

def enter_text(identifier, text, driver, by=By.XPATH):
    element_clickable = EC.element_to_be_clickable((by, identifier))
    element = WebDriverWait(driver, timeout=15).until(element_clickable)
     # Clear the text from the text box (zip code wasn't overwritting)
    element.clear()
    element.send_keys(text)


def is_textbox_empty(driver, textbox_id):
    '''
    This function checks if a text box is empty
    Use this for the income variable so that we don't rewrite it
    every loop
    '''
    textbox = driver.find_element('xpath',textbox_id)
    textbox_value = textbox.get_attribute("value")

    return not bool(textbox_value)