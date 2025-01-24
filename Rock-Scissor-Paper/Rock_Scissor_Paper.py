#Workflow Of Project
#1-Input From User (Rock,Paper,Scissor)
#2-Computer choice using(Random)
#3-Show Results.......
#4-Ask user they want to play again 
import random

# Create list of items
item_list = ['Rock', 'Paper', 'Scissor']

# Initialize scores
user_score = 0
comp_score = 0

# Main loop to ask user if they want to play again
while True:
    # Getting Input From User and showing output
    user_choice = input("Enter your move (Rock, Paper, Scissor): ").capitalize()  # Ensures case consistency
    if user_choice not in item_list:
        print("Invalid input! Please choose Rock, Paper, or Scissor.")
        continue

    comp_choice = random.choice(item_list)

    print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

    # Apply condition for all the possible cases:
    if comp_choice == user_choice:
        print("Match Has Been Tied!")
    elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("Paper Covers Rock = Computer wins")
            comp_score += 1
        else:
            print("Rock Smashes Scissors = You win")
            user_score += 1
    elif user_choice == "Paper":
        if comp_choice == "Scissors":
            print("Scissors Cut Paper = Computer wins")
            comp_score += 1
        else:
            print("Paper Covers Rock = You win")
            user_score += 1
    elif user_choice == "Scissor":
        if comp_choice == "Paper":
            print("Scissors Cut Paper = You win")
            user_score += 1
        else:
            print("Rock Smashes Scissors = Computer wins")
            comp_score += 1

    # Display scores
    print(f"Your Score: {user_score} | Computer Score: {comp_score}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break

