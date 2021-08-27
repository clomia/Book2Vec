import pyautogui, time
import privacy_info
from start import driver, google_login
from surfing import go_to_url
from main_process.capture import CaptureProcess

google_login(privacy_info.EMAIL, privacy_info.PASSWORD, driver=driver)
go_to_url("https://play.google.com/books/reader?id=F_KoDwAAQBAJ&pg=GBS.PT6")


cp = CaptureProcess("laws of human nature")
cp.loop(count=5)

# pyautogui.click(**buttons["next_page"])

time.sleep(1000)
driver.quit()
