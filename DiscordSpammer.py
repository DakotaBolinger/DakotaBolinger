import pyautogui
import webbrowser
import time

message= input("what message do you want to spam")
repeats= int(input("how many times do you want to send this message"))
delay= int(input("how many ms do you wanna wait inbetween messages"))

isLoaded= input("press enter when your discord is loaded")


print("you have five seconds before the spam begins")

time.sleep(5)

for i in range (0,repeats):
    if message !="":
        pyautogui.typewrite(message)
        pyautogui.press("enter")
    else:
        pyautogui.hotkey('ctrl, v')
        pyautogui.press("enter")
    
    time.sleep(delay/1000)

print("Done\n")
