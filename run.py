import os, re, sys
import privacy_info
from start import driver, google_login
from surfing import go_to_url
from main_process.capture import CaptureProcess
from main_process.img_to_text import OcrProcess

_, *is_last = sys.argv

file_list = os.listdir(r"C:/Users/USER/Desktop/Novels/data")
if file_list:
    last_point = max([int(re.sub(r"[^0-9]", "", file_name)) for file_name in file_list])
else:
    last_point = 0

google_login(privacy_info.EMAIL, privacy_info.PASSWORD, driver=driver)
go_to_url("https://play.google.com/books/reader?id=F_KoDwAAQBAJ&pg=GBS.PT6")


cp = CaptureProcess("laws of human nature", start_point=200, scan_range=2)
cp.loop()

if is_last:
    ocr = OcrProcess()
    ocr.transe_pdf()

driver.quit()
os.system("shutdown -s -f")
