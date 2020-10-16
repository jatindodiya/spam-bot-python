import pyautogui
import time
#add delay before we reach to account we want to spam
time.sleep(5)
with open("spambook.txt","r",encoding='utf-8') as file:
    for word in file:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(0.2)



