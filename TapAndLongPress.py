# Import necessary modules from Appium and typing
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
# from appium.webdriver.common.touch_action import TouchAction --> This  class is deprecated
from selenium.webdriver.common.action_chains import ActionChains

# Define the capabilities for the Appium session
cap: Dict[str, Any] = {
    'platformName': 'Android', # Specify the platform (Android)
    'automationName': 'uiautomator2', # Use uiautomator2 for automation
    'deviceName': 'Android', # Name of the device
    'appPackage': 'com.android.contacts', # The app package for the Contacts app
    'appActivity': '.activities.PeopleActivity', # The main activity of the Contacts app
    'language': 'en', # Set language to English
    'locale': 'US' # Set locale to US
}

# URL of the Appium server
url = 'http://localhost:4724'

# Create a new instance of the Appium driver with the defined capabilities
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50) # Set an implicit wait time of 50 seconds for elements to be found

# Find elements with a specific resource ID and print the number of found elements
element = driver.find_elements(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.android.contacts:id/cliv_name_textview"]')
print(len(element)) # Output the number of found elements

# actions = TouchAction(driver)
# actions.tap(element[1]).perform().release()
# actions.long_press(element[1]).perform().release()

# Use ActionChains for touch actions
actions = ActionChains(driver)
# Tap on the second element (index 1) in the list
actions.tap(element[1]).perform().release()
# Perform a long press on the second element (index 1) in the list
actions.long_press(element[1]).perform().release()