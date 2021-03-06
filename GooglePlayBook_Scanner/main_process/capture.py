"""도서를 캡쳐해서 저장하는 프로세스 모듈"""
import pyautogui, time, keyboard, datetime, contextlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class CaptureProcess:

    buttons = {  # * 순서에 의미 있음
        "fullscreen": {"x": -374, "y": 100},
        "display_options": {"x": -277, "y": 26},
        "font_size": {"x": -89, "y": 466},
        "line_spacing": {"x": -89, "y": 588},
        "page_layout": {"x": -89, "y": 822},
        "close": {"x": -61, "y": 99},
        "capture_mode": {"x": 860, "y": 24},
        "capture_start_point": {"x": -1655, "y": 44},
        "capture_end_point": {"x": -259, "y": 1013},
        "capture_end_point_rel": {"xOffset": 1351, "yOffset": 939},
        "capture_result": {"x": 1700, "y": 900},
        "result_tab": {"x": -820, "y": 67},  # * 가변 위치
        "exit_capture_result": {"x": -409, "y": 63},  # *가변 위치
    }

    def __init__(self, book_name, start_point=0, scan_range=100):
        """book_name인자는 영어여야 합니다."""
        if start_point:
            print(f"[{start_point+1}]부터 작업을 시작합니다")

        time.sleep(8)
        self.book_name = book_name
        self.start_point = start_point
        self.scan_range = scan_range

    @contextlib.contextmanager
    def time_logger(self, iter_count):
        start = time.time()
        try:
            yield
        finally:
            term = time.time() - start
            now = datetime.datetime.now()
            wight = 1.5
            print(
                f"[{now.day}일 {now.hour}시{now.minute}분{now.second}초] ({iter_count+1}/{self.scan_range})남은 페이지:{self.scan_range-(iter_count+1)} 남은시간({(term*(self.scan_range-iter_count-1)/60)*wight:.0f}분) -- {self.book_name} [{iter_count+1}]"
            )

    def loop(self):
        """페이지를 넘기면서 프로세스를 반복합니다."""
        self.window_setting()

        for _ in range(self.start_point):
            pyautogui.press("right")

        for i in range(self.scan_range):
            with self.time_logger(iter_count=i):
                self.capture(now_loop=i)
                time.sleep(0.5 + i * 0.1)
                self.save(file_name=f"{self.book_name} [{i+1+self.start_point}]")
                pyautogui.press("right")
                time.sleep(0.5)

    def run(self, file_name):
        """프로세스를 통해 이미지를 캡쳐-저장합니다."""
        self.window_setting()
        self.capture()
        self.save(file_name)

    def window_setting(self):
        pyautogui.click(**self.buttons["fullscreen"])
        time.sleep(2)
        pyautogui.click(**self.buttons["display_options"])
        time.sleep(0.5)
        pyautogui.click(**self.buttons["font_size"], clicks=6)
        # time.sleep(0.5)
        # pyautogui.click(**self.buttons["line_spacing"], clicks=6)
        time.sleep(0.5)
        pyautogui.click(**self.buttons["page_layout"])
        time.sleep(0.5)
        pyautogui.click(**self.buttons["close"])
        time.sleep(0.5)

    def capture(self, now_loop):
        pyautogui.hotkey("win", "shiftleft", "s")
        time.sleep(2)
        pyautogui.click(**self.buttons["capture_mode"])
        time.sleep(0.5)
        pyautogui.moveTo(**self.buttons["capture_start_point"])
        pyautogui.dragTo(**self.buttons["capture_end_point"], duration=2, button="left")
        time.sleep(4 + now_loop * 0.15)
        # 캡쳐 완료 후 결과 누르기 캡쳐 결과는 6초 후에 사라짐
        pyautogui.moveTo(**self.buttons["capture_result"])
        pyautogui.mouseDown()
        pyautogui.mouseUp()

    def save(self, file_name, path=f"{BASE_DIR}/GooglePlayBook_Scanner/data/JPG"):
        """file_name에 한국어는 안됩니다!"""

        time.sleep(3.5)
        pyautogui.click(**self.buttons["result_tab"])
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "s")
        time.sleep(2)
        keyboard.press_and_release("ctrl+L")
        time.sleep(0.2)
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
