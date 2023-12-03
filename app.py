import random

# write 'hello world'to the console
print("Hello World")

# Generate an array of possible options for users. Options are Rock, Paper, Scissors
options = ["Rock", "Paper", "Scissors"]

# save the result of game in two variables, won and lost
won = 0
lost = 0

# create a while loop that loops until the user quits
while True:
    # ask the user to select Rock, Paper, or Scissors
    user_choice = input("Select Rock, Paper, or Scissors or quit to exit: ")
    # if the user quits, exit the program
    if user_choice == "quit":
        break
    # randomly select Rock, Paper, or Scissors for the computer
    computer_choice = random.choice(options)
    # print out the user selection and the computer selection
    print(f"You chose {user_choice}, the computer chose {computer_choice}")
    # if the user selects Rock and the computer selects Scissors, the user wins
    if user_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
        won += 1
    # if the user selects Rock and the computer selects Paper, the user loses
    elif user_choice == "Rock" and computer_choice == "Paper":
        print("You lose!")
        lost += 1
    # if the user selects Paper and the computer selects Rock, the user wins
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You win!")
        won += 1
    # if the user selects Paper and the computer selects Scissors, the user loses
    elif user_choice == "Paper" and computer_choice == "Scissors":
        print("You lose!")
        lost += 1
    # if the user selects Scissors and the computer selects Paper, the user wins
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
        won += 1
    # if the user selects Scissors and the computer selects Rock, the user loses
    elif user_choice == "Scissors" and computer_choice == "Rock":
        print("You lose!")
        lost += 1
    # if the user selects the same as the computer, it is a tie
    else:
        print("It's a tie!")
    # print out the number of wins and losses
    print(f"Wins: {won}, Losses: {lost}")