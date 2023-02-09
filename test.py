import time

sec = 5

while sec > 0:
    print(sec)
    time.sleep(1)
    sec -= 1
    if sec == 0:
        print(
            "timeout"
        )