import random

choices = ['Snake', 'Water', 'Gun']
user_choice = 0
computer_choice = 0

user_score = 0
computer_score = 0

while True:
    user = input("Enter the choices s/w/g : ").lower()

    if(user not in ['s', 'g', 'w']):
        print("\nEnter the right key : ")
        continue

    if(user == 's'):
        user_choice = "Snake"
    elif(user == 'w'):
        user_choice = "Water"
    else :
        user_choice = "Gun"

    computer_choice = random.choice(choices)

    if computer_choice == user_choice:
        print("\nit's draw!\n")
    elif computer_choice != user_choice:
        if computer_choice == "Snake" and user_choice == "Gun" or computer_choice == "Gun" and user_choice == "Water" or computer_choice == "Water" and user_choice == "Snake":
            print("You win!\n")
            user_score+=1
        else:
            print("Computer wins!\n")
            computer_score+=1



    flag = input("Want to continue the game(y/n): ").lower()
    if(flag == 'y'):
        continue
    else:
        break

print("Game over!\n")
print("Your Score : \n" , user_score)
print("Computer Score : \n" , computer_score)

if(user_score > computer_score):
    print("Congratulation! You won the game.")
elif(user_score == computer_score):
    print("It's draw ~_~")
else:
    print("Better luck next time! :)")