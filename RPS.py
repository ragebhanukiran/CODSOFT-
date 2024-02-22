import random 

def RPS(user_choice):
    options = {"a":"rock","b" : "paper","c" : "scissors"}

    computer_choice = random.choice(list(options.values()))

    if user_choice in options.keys() :
        if user_choice == "a" and computer_choice == "b":

            return(f"computer choice is {computer_choice} and user choice is {options.get(user_choice)} \n computer wins")

        elif user_choice == "c" and computer_choice == "a":

            return(f"computer choice is {computer_choice} and user choice is {options.get(user_choice)} \n computer wins")

        elif user_choice == "b" and computer_choice == "c":

            return(f"computer choice is {computer_choice} and user choice is {options.get(user_choice)} \n computer wins")
            
        elif user_choice == computer_choice:
            return(f"computer choice is {computer_choice} and user choice is {options.get(user_choice)} \n its a TIE!!")

        else:
            return(f"computer's choice is {computer_choice} and user choice is {options.get(user_choice)} \n user wins !!")
    else:
        return("invalid input!")
while True :
    print("choose a option : \na) ROCK\nb) PAPER\nc) SCISSORS")
    user_choice = input().strip().lower()
    print(RPS(user_choice))
    print("Press any button to play again else press 0 to exit")
    play = input().strip().lower()
    if play == "0":
        break


    



        
    




