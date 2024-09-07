# Import necessary modules from Appium and typing
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# Define the capabilities for the Appium session
cap: Dict[str, Any] = {
    'platformName': 'Android', # Specify the platform (Android)
    'automationName': 'uiautomator2', # Use uiautomator2 for automation
    'deviceName': 'Android', # Name of the device
    'appPackage': 'com.google.android.dialer', # The app package for the Dialer app
    'appActivity': 'com.android.dialer.main.impl.MainActivity', # The main activity of the Dialer app
    'language': 'en', # Set language to English
    'locale': 'US' # Set locale to US
}

# URL of the Appium server
url = 'http://localhost:4724'

# Create a new instance of the Appium driver with the defined capabilities
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

# Click on the "Recents" tab in the Dialer app
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='Recents']").click()

# Click on the "key pad" button to open the dial pad
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="key pad").click()

# Input the digits 1, 2, 4, 6, and 9 sequentially on the dial pad
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='1']").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='2']").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='4']").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='6']").click()

driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='9']").click()

# Click on the "dial" button to initiate the call
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="dial").click()