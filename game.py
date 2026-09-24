import random 

def play_game():
    lucky_num = random.randint(1,50)

    while True :
        user_num = int(input("Guess the lucky num:"))

        if user_num == lucky_num:
            print("You won. Game Over!")
            break # if the game is completed, no need to move any further. Break finishes the loop.
        elif user_num < lucky_num:
            print("Too Low")
        else :
            print("Too high")

play_game() 