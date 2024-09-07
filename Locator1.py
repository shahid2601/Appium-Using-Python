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
}

# URL of the Appium server
url = 'http://localhost:4724'

# Create a new instance of the Appium driver with the defined capabilities
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

# Find the Chrome application icon using accessibility ID and click on it
el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Chrome')
el.click()

# Find the search bar element in the Chrome browser using XPath and send a URL to it
driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Search or type URL']").send_keys("https://www.google.com/ncr")