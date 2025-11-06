import pyautogui
import time

time.sleep(5)  # Wait for 5 seconds to give you time to switch to the target window
pyautogui.hotkey('ctrl', 'l')  # Example: Open the address bar in a web browser
pyautogui.write('https://mail.google.com/mail/u/0/#inbox')  # Type the URL
pyautogui.press('enter')  # Press Enter to navigate to the URL
time.sleep(10)  # Wait for the page to load

pyautogui.click(x=130, y=328)  # Example: Click at specific coordinates (adjust as needed)
pyautogui.click(x=1227, y=450)  # Click on the username field (adjust coordinates as needed)
time.sleep(2)  # Wait for 2 seconds
pyautogui.write('sriramrajendran.official1@gmail.com')  # Type the email address
time.sleep(1)  # Wait for 1 second
pyautogui.press('enter')  # Press Enter to proceed
time.sleep(2)  # Wait for the password field to appear
pyautogui.click(x=1151, y=541)  # Click on the password field (adjust coordinates as needed)
time.sleep(1)  # Wait for 1 second
pyautogui.write('Mail From PyAutoGUI Bot')  # Type the password
time.sleep(1)  # Wait for 1 second
pyautogui.click(x=1103, y=566)  # Click the login button (adjust coordinates as needed)
time.sleep(2)  # Wait for login to complete
pyautogui.write('Hey Sriram')  # Type a message in the inbox or compose window
pyautogui.press('enter')  # Press Enter to send the message
pyautogui.press('enter')  # Press Enter again if needed
pyautogui.write('This Message is from PyAutoGUI Bot - Which you have learnt Recently From Social Eagle!...')  # Type another message
pyautogui.press('enter')  # Press Enter to send the message
pyautogui.press('enter')  # Press Enter again if needed
pyautogui.press('enter')  # Press Enter to send the message

pyautogui.write('Have a great day!')  # Type a closing message
pyautogui.press('enter')  # Press Enter to send the message
pyautogui.press('enter')  # Press Enter to send the message

pyautogui.write('Thank You :)')  # Type a thank you message
pyautogui.press('enter')  # Press Enter to send the message
pyautogui.write('PyAutoGUI Bot')  # Press Enter to send the message

pyautogui.click(x=1135, y=959)  # Click the close button to close the window (adjust coordinates as needed)