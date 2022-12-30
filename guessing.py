import random
print("WELCOME TO NUMBER GUESSING")
range_number=input("enter the range number: ")
if range_number.isdigit:
    range_number = int(range_number)
else:
    print("**enter a number next time**")
    quit()
random_number = random.randint(0, range_number)
g =0
while True:
    g +=1
    guess=input("what is your guess?: ")
    if guess.isdigit:
        guess = int(guess)
    else:
         print("**enter a number next time**")
         continue
    
    if guess==random_number:
        print("!!CORRECT!!")
        break
    elif guess<random_number:
        print("your answer is below the guess")
    else:
        print("your answer is above the guess")
print("you have guessed",g,"times")

