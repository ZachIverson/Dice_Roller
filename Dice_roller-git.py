import random  # Import the random module

# Function to get user input for the number of dice
def get_number_of_dice():
    while True:
        try:
            num_dice = int(input("Please enter the number of dice you want to roll (1 or more): "))
            if num_dice >= 1:
                return num_dice
            else:
                print("Please enter a number greater than or equal to 1.")
        except ValueError:
            print("Invalid input. Please enter a number greater than or equal to 1.")

# Function to roll and count the total of the dice
def roll_dice(num_dice):
    rolls = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)  
        rolls.append(roll)
    total = sum(rolls)
    return rolls, total

# Main program
def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        print("\nIf you are ready to start the game")
        
        # User input
        num_dice = get_number_of_dice()
        
        # User roll
        user_rolls, user_total = roll_dice(num_dice)
        print(f"\nYou rolled: {user_rolls}")
        print(f"Your total is: {user_total}")
        
        # Computer roll
        computer_rolls, computer_total = roll_dice(num_dice)
        print(f"\nThe computer rolled: {computer_rolls}")
        print(f"The computer's total is: {computer_total}")
        
        # Determine the winner
        if user_total > computer_total:
            print("\nYou win! Congratulations!")
        elif user_total < computer_total:
            print("\nThe computer wins! Better luck next time!")
        else:
            print("\nIt's a tie! ")
        
        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
