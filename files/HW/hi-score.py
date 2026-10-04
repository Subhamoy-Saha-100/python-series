def game():
    score = int(input("Enter the score: "))
    return score

score = game()

with open("hi-score.txt", "r") as f:
    data = f.read()
    
if data == "":
    hi_score = 0
else:
    hi_score = int(data)

if score > hi_score:
    with open("hi-score.txt", "w") as f:
        f.write(str(score))
    print("New Hi-score:", score)
else:
    print("Hi-score:", hi_score)