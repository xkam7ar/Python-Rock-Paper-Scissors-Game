# Rock Paper Scissors Game
import random

def main():
    while True:
        print("ROCK, PAPER, SCISSORS")
        print("Enter your choice: ")
        print("1. ROCK")
        print("2. PAPER")
        print("3. SCISSORS")
        choice = int(input("Enter your choice: "))
        computer = random.randint(1, 3)
        if choice == computer:
            print("Tie")
        elif choice == 1 and computer == 3:
            print("You win!")
        elif choice == 2 and computer == 1:
            print("You win!")
        elif choice == 3 and computer == 2:
            print("You win!")
        else:
            print("You lose!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

    

    
    
     