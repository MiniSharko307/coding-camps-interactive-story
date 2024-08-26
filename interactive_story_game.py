# Interactive Story Game

def start_game():
    print("Welcome to the Interactive Story Game!")
    print("You are about to embark on an adventure where your choices will shape the story.")
    print("Let's begin...\n")
    introduction()

def introduction():
    print("You find yourself at the entrance of a dark forest. It's quiet, too quiet...")
    print("There are two paths ahead of you.")
    print("1. Take the left path.")
    print("2. Take the right path.")
    
    choice = input("Which path do you choose? (1 or 2): ")
    
    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        introduction()

def left_path():
    print("\nYou take the left path and walk deeper into the forest.")
    print("The trees seem to close in around you, but you press on.")
    print("Suddenly, you hear a rustling in the bushes.")
    print("1. Investigate the noise.")
    print("2. Continue walking cautiously.")
    
    choice = input("What do you do? (1 or 2): ")
    
    if choice == "1":
        investigate_noise()
    elif choice == "2":
        continue_walking()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        left_path()

def right_path():
    print("\nYou take the right path and come across a small, peaceful clearing.")
    print("In the center of the clearing is a mysterious glowing stone.")
    print("1. Pick up the stone.")
    print("2. Leave the stone and continue walking.")
    
    choice = input("What do you do? (1 or 2): ")
    
    if choice == "1":
        pick_up_stone()
    elif choice == "2":
        continue_on_path()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        right_path()

def investigate_noise():
    print("\nYou slowly approach the bushes and peer inside.")
    print("A small, harmless rabbit jumps out and scurries away.")
    print("You chuckle at your nervousness and continue on the path.")
    end_game("safe")

def continue_walking():
    print("\nYou decide to ignore the noise and keep walking.")
    print("Suddenly, the ground beneath you gives way, and you fall into a hidden trap!")
    end_game("trapped")

def pick_up_stone():
    print("\nYou pick up the glowing stone, and it pulses with energy.")
    print("You feel a surge of power and knowledge. This stone could be useful.")
    end_game("empowered")

def continue_on_path():
    print("\nYou decide to leave the stone and continue on your journey.")
    print("The forest begins to thin out, and you see the edge of the forest ahead.")
    end_game("safe")

def end_game(outcome):
    if outcome == "safe":
        print("\nCongratulations! You safely navigate the forest and continue your adventure.")
    elif outcome == "trapped":
        print("\nOh no! You fell into a trap and your adventure ends here. Better luck next time!")
    elif outcome == "empowered":
        print("\nWith the power of the stone, you feel ready to face any challenge that comes your way. Your adventure continues!")

    print("Thank you for playing the Interactive Story Game!")
    replay()

def replay():
    choice = input("\nWould you like to play again? (yes or no): ")
    
    if choice.lower() == "yes":
        start_game()
    else:
        print("Goodbye! Thanks for playing.")

# Start the game
start_game()
