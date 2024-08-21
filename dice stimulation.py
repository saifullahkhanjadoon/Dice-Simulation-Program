import random

def roll_dice():
  
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Simulation Program!")
    
    while True:
        user_input = input("\nWould you like to roll the dice? (yes/no): ").strip().lower()
        
        if user_input == 'yes':
            result = roll_dice()
            print(f"You rolled a {result}!")
            
            if result == 6:
                print("Great roll! You got a 6!")
            elif result == 1:
                print("Oh no! You got a 1. Better luck next time.")
        
        elif user_input == 'no':
            print("Thanks for playing! Goodbye!")
            break
        
        else:
            print("Please enter 'yes' or 'no'.")

main()
