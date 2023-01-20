# Description: This file provides helper functions for selecting an item in a dropdown menu,
#   clicking a button, and running Urban's Site Monitor tool for responsible web scraping.
# Original Author: Judah Axelrod
# Date of Creation: January 20, 2023

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
# (If you want to use Chrome instead of Firefox):
# from selenium.webdriver.chrome.service import Chrome
# from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from site_monitor import *
import requests



def click_button(driver, identifier, by=By.XPATH, timeout=15):   
    '''
    This function waits until a button is clickable and then clicks on it using selenium functionality.

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

def select_dropdown(driver, identifier, by=By.XPATH, value=None, index=None):
    '''
    This function clicks on the correct dropdown option in a dropdown object using selenium functionality.
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
    if index is None:
        Select(element).select_by_value(value)
    else:
        Select(element).select_by_index(index)


def run_site_monitor(url, burn_in=20, n=100):
    '''
    This function runs Urban's Site Monitor tool to test for responsible web scraping. It uses the burn-in
    samples to determine a reasonable response time for the website and then prints out a report to
    help users gauge whether they are exceeding that threshold by too much (e.g. whether they are 
    over-burdening the website). 

    NOTE: YOU ALWAYS SHOULD BE RUNNING SITE MONITOR BEFORE IMPLEMENTING A FULL WEB SCRAPING JOB!

    See this Data@Urban post for more details: https://urban-institute.medium.com/sitemonitor-a-tool-for-responsible-web-scraping-e759042e296a

    Inputs:
        burn_in (int): Number of calls to the site to use in determining the reasonable threshold for response time
        n (int): Number of total requests to make to the site (e.g. the x axis of the graph)
    
    Returns:
        None (but will display the graph)
    '''
    sm = SiteMonitor(burn_in=burn_in)

    for i in range(n):
        print(i)
        response = requests.get(url)
        delay = sm.track_request(response)

    # Display the report of response times in graph format
    sm.report('display')