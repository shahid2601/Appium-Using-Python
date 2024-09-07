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
    'appPackage': 'com.android.contacts', # The app package for the Contacts app
    'appActivity': '.activities.PeopleActivity', # The main activity of the Contacts app
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
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create new contact").click()

# Click on the "CANCEL" button to dismiss any initial prompts or dialogs
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='CANCEL']").click()

# Enter the first name "Bruce" into the "First name" field
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='First name']").send_keys("Bruce")

# Enter the last name "Wayne" into the "Last name" field
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Last name']").send_keys("Wayne")

# Enter the phone number "0975468124" into the "Phone" field
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.EditText[@text='Phone']").send_keys("0975468124")

# Click on the "SAVE" button to save the new contact
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text='SAVE']").click()