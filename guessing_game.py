import random

secret_number = random.randint(1,10)

while True:

    print("I am thinking a number between 1 and 10, can you guess it?")

    while True:

        guess = int(input("enter your guess"))
        match guess:
            case _ if guess == secret_number:
                print("Congratlation, you have guessed it right")
                break
            case _ if guess > secret_number:
                print("Oops, too high try again!!")
            case _ if guess < secret_number:
                print("Oops, too low try again!!")
    

    ans = input("Do you want to play again(yes/no)").lower()
    if ans != "yes":
        break

