from pathlib import Path

text = 0
poem_path = Path(__file__).with_name("poem.txt")
text = poem_path.read_text()
if "twinkle" in text.lower():
    print("Twinkle is present")
else:
    print("Twinkle is absent")