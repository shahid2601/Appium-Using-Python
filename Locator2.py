#                                                     Not Working

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

# Find the Chrome app icon using XPath and click on it
el = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Chrome"]')
el.click()

# Find the search bar in the Chrome browser using XPath and enter a URL
driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Search or type URL']").send_keys("https://www.google.com/ncr")