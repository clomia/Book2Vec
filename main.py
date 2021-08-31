import sys, os, re
import numpy as np
import privacy_info
from start import driver, google_login
from surfing import go_to_url
from main_process.capture import CaptureProcess
from main_process.img_to_text import OcrProcess

last_point = np.array(re.findall(r"\d+", os.listdir(r"C:/Users/USER/Desktop/Novels/data"))).astype(int).max()


google_login(privacy_info.EMAIL, privacy_info.PASSWORD, driver=driver)
go_to_url("https://play.google.com/books/reader?id=F_KoDwAAQBAJ&pg=GBS.PT6")


cp = CaptureProcess("laws of human nature")
cp.loop(count=1337)
ocr = OcrProcess()
ocr.transe_pdf()

driver.quit()
