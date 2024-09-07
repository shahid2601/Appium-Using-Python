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
    'appPackage': 'com.android.contacts', # The app package for the Dialer app
    'appActivity': '.activities.PeopleActivity', # The main activity of the Dialer app
    'language': 'en', # Set language to English
    'locale': 'US' # Set locale to US
}

# URL of the Appium server
url = 'http://localhost:4724'

# Create a new instance of the Appium driver with the defined capabilities
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
# Set an implicit wait time of 50 seconds for elements to be found
driver.implicitly_wait(50)

# Click on the button to create a new contact using accessibility ID
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create new contact")
el2.click()

# Click on the "CANCEL" button to dismiss any initial prompts or dialogs
el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='CANCEL']")
el3.click()

# Enter the first name "Steve" into the "First name" field
el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='First name']")
el4.send_keys("Steve")

# Enter the phone number "4754862416" into the "Phone" field
el5 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Phone']")
el5.send_keys("4754862416")

# Click on the "SAVE" button to save the new contact
el6 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='SAVE']")
el6.click()