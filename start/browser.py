""" Chrome 드라이버가 아니라 디버거 Chrome 브라우저인 driver 객체를 제공합니다 """
__all__ = ["driver", "TEMP_DIR"]

import subprocess, shutil, time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# –remote-debugging-port=9222 : 구동하는 크롬의 포트를 알려주는 것
# –user-data-dir=”C:\chrometemp” : 크롬에서 생기는 쿠키와 캐쉬파일을 저장하는 곳

TEMP_DIR = "C:\chrometemp"

#! 브라우저는 생성될때마다 초기화 상태입니다
shutil.rmtree(TEMP_DIR)

subprocess.Popen(
    fr"C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir={TEMP_DIR}"
)


options = Options()
options.add_experimental_option(
    "debuggerAddress",
    "127.0.0.1:9222",
)

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split(".")[0]
try:
    driver = webdriver.Chrome(f"./{chrome_ver}/chromedriver.exe", options=options)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f"./{chrome_ver}/chromedriver.exe", options=options)

driver.set_window_position(-1500, 0)
driver.maximize_window()
