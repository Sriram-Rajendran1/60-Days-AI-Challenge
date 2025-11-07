import pyautogui
import time
import webbrowser

webbrowser.open('https://web.whatsapp.com/')
time.sleep(15)  # Wait for WhatsApp Web to load and for user to scan QR code

contact_name = "SE - AI-B3 - 2"  # Replace with the contact or group name
message = "One Week Completed Successfully! - PyAutoGUI Bot :)"  # Replace with your message      

pyautogui.click(x=471, y=305)  # Click on the search bar (coordinates may vary)
time.sleep(2)   

pyautogui.write(contact_name)  # Type the contact name
time.sleep(2)
pyautogui.press('enter')  # Open the chat
time.sleep(2)
pyautogui.click(x=1129, y=958)  # Click on the message input box (coordinates may vary)
pyautogui.write(message)  # Type the message
pyautogui.press('enter')  # Send the message
time.sleep(2)
print("Message sent successfully!")
