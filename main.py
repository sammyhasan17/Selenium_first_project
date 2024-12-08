from selenium import webdriver
from selenium.webdriver.common.by import By  # Import By class to locate elements
import time  # Import the time module to add delays

# Step 1: Set up and launch the browser
# Initialize the Edge browser driver (ensure the EdgeDriver executable is in your PATH)
driver = webdriver.Edge()

# step 2 implicit wait
driver.implicitly_wait(0.5)

# Step 3: Navigate to the target web page
# Open the Selenium demo web form page
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Get and print the title of the web page (optional)
title = driver.title
print(f"Page Title: {title}")


time.sleep(1) 

# Step 4: Locate and interact with web elements
# Locate the text box by its 'name' attribute and input text
text_box = driver.find_element(by=By.NAME, value="my-text")
text_box.send_keys("cool")  # Enter the text "Selenium" into the text box

time.sleep(1) # Wait for 1 second to see the entered text in the text box

# Locate the submit button using a CSS selector and click it
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit_button.click()  # Simulate a click action on the submit button

# Step 5: Retrieve information after form submission
# Locate the element that displays the response message (replace 'message' with the correct ID)
message_element = driver.find_element(by=By.ID, value="message")  # Update the locator based on your HTML structure

# Extract the text content of the located message element
text = message_element.text
print(f"Message Text: {text}")  # Print the retrieved text to the console

# Step 6: Close the browser
# Quit the browser session to free up resources
driver.quit()
