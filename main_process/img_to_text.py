import pyautogui, keyboard, time


class OcrProcess:

    buttons = {  # * 순서에 의미 있음
        "edit_btn": {"x": 1262, "y": 360},  # * 가변 위치
        "to_pdf_btn": {"x": 116, "y": 383},
        "resist_btn": {"x": 568, "y": 542},
        "save_btn": {"x": -840, "y": 857},
        "save_window": {"x": -816, "y": 415},
        "path_setting": {"x": 417, "y": 857},
        "apply_btn": {"x": 847, "y": 858},
    }

    def transe_pdf(self, path=r"C:\Users\USER\Desktop\Novels\data"):
        pyautogui.hotkey("win", "s")
        pyautogui.write("ALPDF")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(5)
        pyautogui.click(**self.buttons["edit_btn"])
        time.sleep(3)
        pyautogui.click(**self.buttons["to_pdf_btn"])
        time.sleep(0.5)
        pyautogui.click(**self.buttons["resist_btn"])
        time.sleep(8)
        pyautogui.click(**self.buttons["save_window"])  # 창 선택용
        keyboard.press_and_release("ctrl+L")
        pyautogui.write(path, interval=0.01)
        pyautogui.press("enter")
        pyautogui.press("tab", presses=4, interval=0.5)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.click(**self.buttons["save_btn"])
        time.sleep(0.5)
        pyautogui.click(**self.buttons["path_setting"])
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.5)
        pyautogui.write(path, interval=0.01)
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.click(**self.buttons["apply_btn"])


if __name__ == "__main__":
    OcrProcess().transe_pdf()

# 6622 6972
