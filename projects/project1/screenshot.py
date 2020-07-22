import time
import pyautogui
def screenshot():
    name=int(round(time.time()*1000))
    name='C:/Users/Administrator/Desktop/20projects/projects/project1/{}.jpg'.format(name)
    time.sleep(5)
    img=pyautogui.screenshot(name)
    img.show()
screenshot()

