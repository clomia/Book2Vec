import pyautogui


def go_to_url(url):
    """브라우저가 선택된 상태에서 url로 이동합니다."""
    pyautogui.hotkey("ctrl", "l")
    pyautogui.write(url, interval=0.025)
    pyautogui.press("enter")
