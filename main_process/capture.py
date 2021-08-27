"""도서를 캡쳐해서 저장하는 프로세스 모듈"""
import pyautogui, time


class CaptureProcess:

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
        "capture_result": {"x": 1700, "y": 900},
        "result_tab": {"x": -877, "y": 114},  # * 가변 위치
        "exit_capture_result": {"x": -616, "y": 115},  # *가변 위치
    }

    def __init__(self, book_name, wait=8):
        """book_name인자는 영어여야 합니다."""
        time.sleep(wait)
        self.book_name = book_name

    def loop(self, count=20):
        """페이지를 넘기면서 프로세스를 반복합니다."""
        self.window_setting()
        for i in range(count):
            self.capture()
            self.save(file_name=f"{self.book_name} [{i}]")
            pyautogui.press("right")
            time.sleep(0.6)

    def run(self, file_name):
        """프로세스를 통해 이미지를 캡쳐-저장합니다."""
        self.window_setting()
        self.capture()
        self.save(file_name)

    def window_setting(self):
        pyautogui.click(**self.buttons["fullscreen"])
        time.sleep(0.5)
        pyautogui.click(**self.buttons["display_options"])
        time.sleep(0.5)
        pyautogui.click(**self.buttons["font_size"], clicks=6)
        time.sleep(0.5)
        pyautogui.click(**self.buttons["line_spacing"], clicks=6)
        time.sleep(0.5)
        pyautogui.click(**self.buttons["page_layout"])
        time.sleep(0.5)
        pyautogui.click(**self.buttons["close"])
        time.sleep(0.5)

    def capture(self):
        pyautogui.hotkey("win", "shiftleft", "s")
        time.sleep(1.5)
        pyautogui.click(**self.buttons["capture_mode"])
        time.sleep(0.5)
        pyautogui.moveTo(**self.buttons["capture_start_point"])
        pyautogui.dragTo(**self.buttons["capture_end_point"], duration=2, button="left")
        time.sleep(1)
        # 캡쳐 완료 후 결과 누르기
        pyautogui.moveTo(**self.buttons["capture_result"], duration=1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()

    def save(self, file_name, path=r"C:\Users\USER\Pictures\test"):
        """file_name에 한국어는 안됩니다!"""

        time.sleep(1)
        pyautogui.click(**self.buttons["result_tab"])
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "s")
        time.sleep(1)
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.5)
        pyautogui.write(path, interval=0.02)
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.press("tab", presses=5, interval=0.1)
        time.sleep(0.5)
        pyautogui.write(message=rf"{file_name}.jpg", interval=0.02)
        time.sleep(0.5)
        pyautogui.press("tab", presses=3, interval=0.1)
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.click(**self.buttons["exit_capture_result"])
        time.sleep(0.7)
