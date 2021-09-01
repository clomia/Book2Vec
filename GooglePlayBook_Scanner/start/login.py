""" 로그인을 진행하면 캐시파일이 생성되서 이후 로그인 없이 진행 가능하다 """

import time
import pyautogui


def google_login(email, password, driver):

    driver.implicitly_wait(10)
    driver.get(r"https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    pyautogui.write(email, interval=0.025)
    pyautogui.press("enter")
    time.sleep(2.65)
    pyautogui.write(password, interval=0.025)
    pyautogui.press("enter")
