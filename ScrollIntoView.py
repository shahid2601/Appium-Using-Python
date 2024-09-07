# Import necessary modules from Appium, Selenium, and typing
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

# Define the capabilities for the Appium session
cap: Dict[str, Any] = {
    'platformName': 'Android', # Specify the platform (Android)
    'automationName': 'uiautomator2', # Use uiautomator2 for automation
    'deviceName': 'Android', # Name of the device
    'appPackage': 'com.hmh.api', # The app package for the application under test
    'appActivity': '.ApiDemos', # The main activity of the app
    'language': 'en', # Set language to English
    'locale': 'US' # Set locale to US
}

# URL of the Appium server
url = 'http://localhost:4724'

# Create a new instance of the Appium driver with the defined capabilities
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
# Set an implicit wait time of 50 seconds for elements to be found
driver.implicitly_wait(50)

# Check if the "Continue" button is displayed, then click it and handle the subsequent alert
if driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').is_displayed():
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()
    wait = WebDriverWait(driver, 10) # Create a WebDriverWait instance for explicit waits
    el1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/button1"))) # Wait until the element with ID "android:id/button1" is present
    el1.click() # Click on the element

# Wait for and interact with elements in the "App" and "Activity" sections
wait1 = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
el2 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='App']"))) # Wait until the "App" text view is present
el2.click() # Click on the "App" text view

el3 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Activity']"))) # Wait until the "Activity" text view is present
el3.click() # Click on the "Activity" text view

# Scroll to the element with text "Wallpaper" using UiScrollable
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                  'true)).scrollIntoView(new UiSelector().text("Wallpaper"))')