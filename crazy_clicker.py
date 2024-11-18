import keyboard
import pyautogui
import threading
import time

# Initial activation state
is_active = False

# Function to toggle the state
def toggle_activation():
    global is_active
    is_active = not is_active
    if is_active:
        print("Activated")
        start_clicking()
    else:
        print("Deactivated")

# Function to simulate left mouse clicks every second
def start_clicking():
    def click_loop():
        while is_active: 
            pyautogui.click()
            time.sleep(0.005)  # Wait for 1 second between clicks

    # Start the clicking in a new thread so it doesn't block the main program
    threading.Thread(target=click_loop).start()

# Attach the spacebar to the toggle function
keyboard.on_press_key("space", lambda _: toggle_activation()) 

# Keep the program running
keyboard.wait("esc")  # Press "esc" to exit the program
