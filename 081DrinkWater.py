import time
import pyttsx3
import ctypes  # For pop-up message box

# Wait for 2 seconds
time.sleep(2)

# Text-to-speech
engine = pyttsx3.init()
engine.say("Hi , Drink Water!")
engine.runAndWait()

# Pop-up alert
ctypes.windll.user32.MessageBoxW(0, "This is your daily reminder to Drink Water!", "Reminder", 1)
