print("WELCOME TO THE OMEGA COMPUTER QUIZ")
player=input("enter your name: ").upper()
playing=input("Do you want to play the omega computer quiz?? ").lower()
if playing=="yes":
    print("let us play!! ")
else:
    quit()

score= 0
print("!QUESTION ONE!")
answer=input("CPU in full: ").lower()
if answer =="central processing unit":
    print("!!correct!!")
    score +=1
else:
    print("**wrong")

print("!QUESTION TWO!")
answer=input("Os in full: ").lower()
if answer =="operating system":
    print("!!correct!!")
    score +=1
else:
    print("**wrong")

print("!QUESTION THREE!")
answer=input("PC in full: ").lower()
if answer =="personal computer":
    print("!!correct!!")
    score +=1
else:
    print("**wrong")

print("!QUESTION FOUR!")
answer=input("ROM in full: ").lower()
if answer =="read only memory":
    print("!!correct!!")
    score +=1
else:
    print("**wrong")

print("!QUESTION FIVE!")
answer=input("RAM in full: ").lower()
if answer =="random access memory":
    print("!!correct!!")
    score +=1
else:
    print("**wrong")

print(" YOU ARE DONE :) ")
print("you have scored "+str(score)+" out of five questions")
print("which",str((score/5)*100)+"%")
