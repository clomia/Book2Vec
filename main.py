import pyautogui, time
from start import driver, google_login
import privacy_info

google_login(privacy_info.EMAIL, privacy_info.PASSWORD, driver=driver)

pyautogui.hotkey("ctrl", "l")
pyautogui.write("https://play.google.com/books/reader?id=F_KoDwAAQBAJ&pg=GBS.PT6", interval=0.025)
pyautogui.press("enter")


buttons = {  # * 순서에 의미 있음
    "fullscreen": {"x": -374, "y": 100},
    "display_options": {"x": -277, "y": 26},
    "font_size": {"x": -89, "y": 466},
    "line_spacing": {"x": -89, "y": 588},
    "page_layout": {"x": -89, "y": 822},
    "close": {"x": -61, "y": 99},
    "capture_mode": {"x": 860, "y": 24},
    "capture_start_point": {"x": -1643, "y": 110},
    "capture_end_point": {"x": -292, "y": 949},
    "capture_end_point_rel": {"xOffset": 1351, "yOffset": 939},
    "next_page": {"x": -35, "y": 1056},
    "capture_result": {"x": 1700, "y": 900},
    "exit_capture_result": {"x": -695, "y": 50},  # *가변 위치
}
time.sleep(3)
pyautogui.click(**buttons["fullscreen"])
time.sleep(1)
pyautogui.click(**buttons["display_options"])
time.sleep(1)
pyautogui.click(**buttons["font_size"], clicks=6)
time.sleep(1)
pyautogui.click(**buttons["line_spacing"], clicks=6)
time.sleep(1)
pyautogui.click(**buttons["page_layout"])
time.sleep(1)
pyautogui.click(**buttons["close"])
time.sleep(1)

for i in range(4):

    pyautogui.hotkey("win", "shiftleft", "s")
    time.sleep(1)
    pyautogui.click(**buttons["capture_mode"])
    time.sleep(1)
    pyautogui.moveTo(**buttons["capture_start_point"])
    time.sleep(1)
    pyautogui.dragTo(**buttons["capture_end_point"], duration=2, button="left")
    time.sleep(1)
    pyautogui.moveTo(**buttons["capture_result"], duration=1)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.press("tab", presses=10, interval=0.5)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "l")
    time.sleep(1)
    pyautogui.write(r"C:\Users\USER\Pictures\test")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("tab", presses=5, interval=0.5)
    time.sleep(1)
    pyautogui.write(f"{i}.jpg")
    time.sleep(1)
    pyautogui.press("tab", presses=3, interval=0.5)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(**buttons["exit_capture_result"])
    time.sleep(1)

    pyautogui.click(**buttons["next_page"])

time.sleep(1000)
driver.quit()
