import time

with open("this.txt", "r") as f:
    for line in f:
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.07)
