# import pyttsx3
# import time

# engine = pyttsx3.init()

# # Set Zira (female) voice
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# # Say intro first
# # engine.say('Hi! I am Zira, your female virtual assistant.')
# # engine.runAndWait()  # Force execution before continuing

# # List of names
# names = ['Harry Potter', 'Ron Weasley', 'Hermione Granger', 'Dumbledore', 'Hagrid', 'Sirius']

# # Say each name one by one, with a pause
# for name in names:
#     engine.say(name)
# engine.runAndWait()   # Run after each name
#            # Optional: pause between names

# # # Keep the window open (for some IDEs)
# # input("Press Enter to exit...")
# for i in range(10):
#     print(i)

# the above code doesnt work properly

from gtts import gTTS
import os

names = ['Harry Potter', 'Ron Weasley', 'Hermione Granger', 'Dumbledore', 'Hagrid', 'Sirius']
text = "Hi! I am your assistant. Here are the names: " + ", ".join(names)

tts = gTTS(text)
tts.save("output.mp3")
os.system("start output.mp3")  # Windows

