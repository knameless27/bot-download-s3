import pyautogui
import time

class SaludoCola:
    def __init__(self):
        self.widthScreen, self.hightScreen = pyautogui.size()
        self.dots = pyautogui.locateOnScreen("./assets/dots.png")
        pass
    
    def downloadFile(self):
        pyautogui.press(["tab", "tab"])
        pyautogui.press("enter")
        pyautogui.press(["down","down","down","down","down","down","down","enter"])
        time.sleep(2)
        pyautogui.press("esc")
    
    def decir_frase(self):
        time.sleep(2)
        pyautogui.click()
        while True:
            self.downloadFile()

objeto_saludo = SaludoCola()

objeto_saludo.decir_frase()
