import sys, subprocess

_, command = sys.argv

prefix = ["env\Scripts\python.exe"]

commands = {
    #! autopygui 모델이 서브프로세스에서는 재대로 작동을 안하더라
    # "scan": lambda: subprocess.run(prefix + ["GooglePlayBook_Scanner/run.py"]),
    # "scan_and_ocr": lambda: subprocess.run(prefix + ["GooglePlayBook_Scanner/run.py", "ocr"]),
}

print(list(commands.keys()))
commands[command]()
