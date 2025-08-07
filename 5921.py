from gtts import gTTS
import os

# Urdu text
text = "ماما جی، سندس سے بات کر رہی ہیں۔ سندس آپ کا دن کیسا گزر رہا ہے؟ آپ کو یہ سن کر کیسا لگا؟"

# Create gTTS object with Urdu language
tts = gTTS(text=text, lang='ur')
tts.save("output.mp3")

# Play the audio (Windows)
os.system("start output.mp3")
