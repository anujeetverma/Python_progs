import pyautogui
import time
import os
import psutil

def is_whatsapp_running():
    """Check if WhatsApp is running on the system."""
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] == 'WhatsApp.app':  # For macOS, the process name may vary
            return True
    return False

def send_whatsapp_message(contact_name, message, delay=2, use_down_arrow=False, typing_speed=0.1):
    # Open WhatsApp Desktop app if it's not running
    if not is_whatsapp_running():
        os.system("open -a WhatsApp")  # Open WhatsApp Desktop on macOS
        time.sleep(5)                  # Wait for WhatsApp to open
    else:
        print("WhatsApp is already open.")

    # Search for the contact in WhatsApp
    pyautogui.hotkey('command', 'f', interval= 1)  # Open search in WhatsApp (Cmd + F)
    time.sleep(1)
    pyautogui.write(contact_name)     # Type the contact's name
    time.sleep(3)                     # Wait for the contact search results to appear
    pyautogui.press("enter")
    time.sleep(1)
    # Optionally press the down arrow if needed to select the contact
    if use_down_arrow:
        pyautogui.press("down")       # First down press
        time.sleep(1)
        pyautogui.press("down")       # First down press
        time.sleep(1)
        
        
    pyautogui.press('enter')         # Press Enter to select the contact and open chat
    time.sleep(2)
    pyautogui.press('space')
    time.sleep(2)

    # Send the message with adjusted typing speed
    pyautogui.write(message) # Type the message with a delay between each character
    pyautogui.press('enter')         # Press Enter to send the message
    time.sleep(1)
    time.sleep(delay)                 # Wait before sending the next message

# Example usage
contact_name = "Aneek IIIT"  # Replace with the actual contact name
message = "Hello"
for i in range(1, 10):
    send_whatsapp_message(contact_name, message, use_down_arrow=True)  # Set to True if needed
    time.sleep(10)  # Adjust the delay between messages
