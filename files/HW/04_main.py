

with open("donkey.txt", "r", encoding="utf-8") as f:
    line = f.read()

line = line.replace("donkey", "#####")

with open("donkey.txt", "w", encoding="utf-8") as f:
    f.write(line)

