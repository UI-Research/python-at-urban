# Description: This file provides a demo of how to click on dropdowns and buttons on an interactive website
#   in order to download a data file using selenium functionality.
# Original Author: Judah Axelrod
# Date of Creation: January 20, 2023

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
import importlib
utils = importlib.import_module('web-scraping-utils')



url = "https://data.cms.gov/tools/mapping-medicare-disparities-by-population"

# Set up selenium driver 
service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

# Navigate to page 
driver.get(url)
# Switch to iframe
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@title="population"]')))

# Set the dropdown options we want to select
measure = 'e'
index = 0
dual = 'null'
sex = 'null'
age = 'null'
race = '1'

# Select all the dropdown options
utils.select_dropdown(driver=driver, identifier='year', by=By.ID, value='9') # '9' --> Year = 2019
utils.select_dropdown(driver=driver, identifier='geography', by=By.ID, value='s') # 's' --> Geography = State/Territory
utils.select_dropdown(driver=driver, identifier='measure', by=By.ID, value=measure)
utils.select_dropdown(driver=driver, identifier='adjust', by=By.ID, value='3') # '3' --> Adjustment = smoothed actual
utils.select_dropdown(driver=driver, identifier='condition', by=By.ID, value=None, index=index)
utils.select_dropdown(driver=driver, identifier='dual', by=By.ID, value=dual)
utils.select_dropdown(driver=driver, identifier='sex_code', by=By.ID, value=sex)
utils.select_dropdown(driver=driver, identifier='age_group', by=By.ID, value=age)
utils.select_dropdown(driver=driver, identifier='race_code', by=By.ID, value=race)

# Click button
utils.click_button(driver=driver, identifier='data_download', by=By.ID)
