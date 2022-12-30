print("WELCOME TO ADVENTURE MIND GAME")
name=input("Enter your name: ").lower()
print("let us play",name)
answer=input("which areas would want to start from?(downtown/uptown): ").lower()
if answer =="downtown":
    answer=input ("will you practice in 'gardening' or 'market'?:  ").lower()
    if answer == "gardening":
        answer=input ("will e gradening for food to 'eat' or 'sell'?:  ").lower()
        if answer == "eat":
            print("u will eat the food but not have money for other basic needs(YOU LOSE)")
        else:
            print("u will sell the food ad have nothing to eat(YOU LOSE) ")

    
    elif answer=="market":
        answer=input ("will you do in the market?'sell','buy': ").lower()
        if answer=="sell":
            print("u will get money")
        else:
            print("you money will get done.will go to the bank(yes/no)").lower()
            if answer=="yes":
                print ("you get more money you WIN")
            elif answer=="no":
                print("you lose") 
            else:
                print("not valid") 


elif answer =="uptown":
    answer=input("will you practice in 'trading' or 'marketing'?:  ").lower()
    if answer == "marketing":
        print("you do marketing and generate alot of money(YOU WIN!!)")
    
    elif answer=="Trading":
        answer=input ("will you trade in?'food','clothes': ").lower()
        if answer=="food":
            print("u will get money(YOU WIN!!)")
        else:
            print("do you have ready market for your goods?(yes/no): ").lower()
            if answer=="yes":
                print ("you get more money (you WIN!!)")
            elif answer=="no":
                print("you lose") 
            else:
                print("not valid") 

else:  
    print("not valid you are out")

print("thank youfor trying "+name)