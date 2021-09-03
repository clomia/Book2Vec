import pyautogui, time


def capture(bought=False):
    for _ in range(50):
        pyautogui.press("f3")
        time.sleep(0.8)
        if bought:
            pyautogui.click(-40, 1052)
        else:
            pyautogui.click(-187, 1052)
        time.sleep(0.8)


capture(bought=False)
