import random;

number=random.randint(1,9)
chances=0

print("Guess A Number Between 1 To 9: ")



while chances < 5:
    guess=int(input("Enter Your Guess: "))

    if guess == number:
       print("You Won")
       break
    elif guess < number:
        print("Your Guess was Too Low")
    else:
        print("Your Guess was Too Hight")     
    chances=chances+1

if not chances < 5:
    print("You Lose, The Number Is ",number)





    