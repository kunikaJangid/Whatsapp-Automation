pip install pywhatkit
pip install selenium


import pywhatkit as kit
from datetime import datetime

# Set the target phone number and message
phone_num = '+1234567890'
message = 'Hello, this is an automated message!'

# Schedule the message to be sent at a specific time
now = datetime.now()
hour = now.hour
minute = now.minute + 1  # Send the message 1 minute from now
kit.sendwhatmsg(phone_num, message, hour, minute)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (ensure you have the correct driver for your browser)
driver = webdriver.Chrome('chromedriver_path')  # Download the driver and specify the path

# Open WhatsApp Web
driver.get('https://web.whatsapp.com/')
input("Scan the QR code and press Enter after logging in...")

# Click on your profile picture to open the profile
driver.find_element_by_xpath('//div[@title="Your Name"]').click()

# Click on the camera icon to change profile picture
driver.find_element_by_xpath('//div[@class="_1j3xh"]').click()

# Upload your profile picture
image_path = 'path_to_your_image.png'  # Replace with the path to your image
input_box = driver.find_element_by_xpath('//input[@type="file"]')
input_box.send_keys(image_path)

# Wait for a moment for the image to upload
time.sleep(5)

# Close the browser
driver.quit()




import pywhatkit as kit

# Set the status text or image file path
status_text = "This is my automated status!"
image_path = "path_to_your_image.png"  # Replace with the path to your image

# Update status with text
kit.text_to_handwriting(status_text, 'status_text.png')
kit.update_status('status_text.png')

# Update status with an image
kit.update_status(image_path)
