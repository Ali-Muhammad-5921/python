import time

timestamp = time.strftime("%H:%M:%S")
hours = int(time.strftime("%H"))

if(hours > 0 and hours < 12):
    print("Good Morning :)")
elif(hours > 12 and hours < 17):
    print("Good AfterNoon :)")
else:
    print("Good Evening :)")

print("The current time is : ", timestamp)