import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

# List all voices
for index, voice in enumerate(voices):
    print(f"Voice {index}:")
    print(f"  ID: {voice.id}")
    print(f"  Name: {voice.name}")
    print(f"  Gender: {voice.gender if hasattr(voice, 'gender') else 'N/A'}")
    print()
