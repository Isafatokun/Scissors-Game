import random

def user():
    while True:
        print("\nWelcome to the Game!")
        user_choice = input('Enter "R" for "rock", "P" for "paper", "S" for "scissors"  ').upper()

        if user_choice == "R" or user_choice == "S" or user_choice == "P":
            if user_choice == "R":
                user_choice = "rock"
            elif user_choice == "P":
                user_choice = "paper"
            elif user_choice == "S":
                user_choice = "scissors"
            return user_choice
            continue
        else:
            print("Wrong Input, please try again")
            continue    

def computer():
    computer_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_options)
    return computer_choice

def play():
    while True:
        user_choice = user()
        computer_choice = computer()
        print(f"Player ({user_choice}), Computer: ({computer_choice})")

        if computer_choice == user_choice:
            print("Its a tie")
            continue
        elif computer_choice == "rock" and user_choice == "scissors":
            print("Computer wins")
            break

        elif computer_choice == "scissors" and user_choice == "rock":
            print("User wins")
            break

        elif computer_choice == "paper" and user_choice == "rock":
            print("Computer wins")
            break

        elif computer_choice == "rock" and user_choice == "paper":
            print("User wins")  
            break
            
        elif computer_choice == "scissors" and user_choice == "paper":
            print("Computer wins")
            break
        elif computer_choice == "paper" and user_choice == "scissors":
            print("User wins")
            break

play()
