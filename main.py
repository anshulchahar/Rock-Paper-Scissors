import random


def retry():
    re = input("Do you want to retry : ")
    if re == "no" :
       return False
    elif re == "yes" :
        return True

is_true = True
while is_true :
    com_move = random.randint(1, 3)
    my_move = int(input("Enter your move 1. Rock , 2. Paper , 3. Scissors"))
    if com_move == 1 :
        if my_move == 1 :
            print("Its a Draw play again")
        elif my_move == 2 :
            print("You win")
            is_true = retry()

        else :
            print("you lose")
            is_true = retry()

    elif com_move == 2 :
        if my_move == 2:
            print("Its a Draw play again")
        elif my_move == 3:
            print("You win")
            is_true = retry()
        else:
            print("you lose")
            is_true = retry()

    else :
        if my_move == 3:
            print("Its a Draw play again")
        elif my_move == 1:
            print("You win")
            is_true = retry()
        else:
            print("you lose")
            is_true = retry()
