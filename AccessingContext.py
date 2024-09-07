# Import necessary modules from Appium, Selenium, and typing
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait # Import WebDriverWait for explicit waits
from selenium.webdriver.support import expected_conditions as EC # Import Expected Conditions for waits

# Define the capabilities for the Appium session
cap: Dict[str, Any] = {
    'platformName': 'Android', # Specify the platform as Android
    'automationName': 'uiautomator2', # Use uiautomator2 for automation
    'deviceName': 'Android', # Name of the device
    'appPackage': 'com.socialnmobile.dictapps.notepad.color.note', # The app package for the ColorNote app
    'appActivity': 'com.socialnmobile.colornote.activity.Main', # The main activity of the ColorNote app
    'language': 'en', # Set language to English
    'locale': 'US' # Set locale to US
}

# URL of the Appium server
url = 'http://localhost:4724'

# Create a new instance of the Appium driver with the defined capabilities
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50) # Set an implicit wait time of 50 seconds for finding elements

# Initialize explicit wait with a timeout of 10 seconds
wait = WebDriverWait(driver, 10)
el1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "(//android.widget.Button[@text='SKIP'])")))
el1.click() # Click the "SKIP" button to bypass any introductory screen

# Wait until the fifth icon in the list is present and click it
el2 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "(//android.widget.ImageView["
                                                                 "@resource-id='com.socialnmobile.dictapps.notepad.color.note:id/icon'])[5]")))
el2.click()# Click the fifth icon (presumably related to the "Like us on Facebook" option)
el3 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "(//android.widget.TextView[@text='Like us on "

                                                                 "Facebook'])")))
el3.click() # Click the "Like us on Facebook" option

# Print the current contexts available within the app (e.g., NATIVE_APP, WEBVIEW)
print(driver.contexts)
print(driver.context)

# Wait until the "Log in" button is present and print its text
e14 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "(//android.widget.Button[@text='Log in'])")))
print(e14.text) # Output the text of the "Log in" button to the console

e14 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "(//android.widget.Button[@text='Log in'])")))
