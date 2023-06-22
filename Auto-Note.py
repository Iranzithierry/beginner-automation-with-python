import pyautogui
import time

# Delay before starting (in seconds)
time.sleep(3)

# Open the text editor (example: Notepad on Windows)
pyautogui.press('win')
pyautogui.typewrite('Notepad')
pyautogui.press('enter')

# Wait for the editor to open
time.sleep(2)

# Type a message
message = "Hello, automation!"
pyautogui.typewrite(message)

# Save the file (example: Ctrl + S)
pyautogui.hotkey('ctrl', 's')

# Wait for the save dialog to appear
time.sleep(2)

# Type the file name and press Enter
file_name = "automated_message.txt"
pyautogui.typewrite(file_name)
pyautogui.press('enter')

# Close the text editor (example: Alt + F4)
pyautogui.hotkey('alt', 'f4')
