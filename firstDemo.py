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
    'appPackage': 'com.android.settings', # The app package to be launched
    'appActivity': '.Settings', # The main activity of the app
    'language': 'en', # Set language to English
    'locale': 'US' # Set locale to US
}

# URL of the Appium server
url = 'http://localhost:4724'

# Create a new instance of the Appium driver with the defined capabilities
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

# Find the element with the text "Battery" using XPath
el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
el.click() # Click on the found element

driver.quit() # Quit the Appium driver and close the session