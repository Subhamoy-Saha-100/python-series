import os

folder = r"D:\Aiml\python\files\HW\multiplication table"
os.makedirs(folder, exist_ok=True)

def multiple_table(x):
    nums = []
    for i in range(1, 11):
        nums.append(i * x)
    return nums


for i in range(2,21):
    filename = f"{folder}/Table_{i}.txt"
    table = multiple_table(i)
    
    with open(filename, "w") as f:
        f.write(str(table))

print("Multiplication tables from 2 to 20 have been created!")

