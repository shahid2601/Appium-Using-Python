from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

# Desired capabilities for the Android device and the target app (Contacts app)
cap: Dict[str, Any] = {
    'platformName': 'Android', # Target platform is Android
    'automationName': 'uiautomator2', # Using UiAutomator2 for automation
    'deviceName': 'Android', # Name of the device (can be a real device or emulator)
    'appPackage': 'com.android.contacts', # The package name of the Contacts app
    'appActivity': '.activities.PeopleActivity', # The activity to start (main activity of Contacts app)
    'language': 'en', # Setting the language to English
    'locale': 'US' # Setting the locale to US
}

# The URL where Appium server is running (local server in this case)
url = 'http://localhost:4724'

# Initializing the Appium driver with the desired capabilities
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
# Implicit wait to handle element loading delays
driver.implicitly_wait(50)

# Check if the "Continue" button is displayed and click it if found
if driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').is_displayed():
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]').click()

    # Explicit wait for the next element (button with ID "android:id/button1") to become visible
    wait = WebDriverWait(driver, 10)
    el1 = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/button1")))
    el1.click()

# Create another explicit wait with exception handling for visibility of elements
wait1 = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

# Wait until the element "App" text is located, then click it
el2 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='App']")))
el2.click()

# Wait until the element "Activity" text is located, then click it
el3 = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Activity']")))
el3.click()

# Perform a scroll action using the UiScrollable Android UIAutomator method
# Scroll vertically and click the second element in the list (index 1)
driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable('
                                                  'true)).setAsVerticalList)')[1].click()