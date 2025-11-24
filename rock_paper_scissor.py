import random

print("Welcome to Rock–Paper–Scissors Game!")

choices = ["rock", "paper", "scissor"]

user_score = 0
computer_score = 0
tie_score = 0

while True:
    user_choice = input("Enter rock, paper, or scissor (or 'exit' to quit): ").lower()

    if user_choice == "exit":
        print("\nFinal Scoreboard:")
        print("--------------------")
        print(f"You      : {user_score}")
        print(f"Computer : {computer_score}")
        print(f"Ties     : {tie_score}")
        print("--------------------")
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice! Try again.\n")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Result: It's a tie!\n")
        tie_score += 1

    elif (user_choice == "rock" and computer_choice == "scissor") or          (user_choice == "paper" and computer_choice == "rock") or          (user_choice == "scissor" and computer_choice == "paper"):
        print("Result: You win! 🎉\n")
        user_score += 1

    else:
        print("Result: Computer wins! 🤖\n")
        computer_score += 1

    print("Scoreboard:")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")
    print(f"Ties     : {tie_score}")
    print("-" * 20)
