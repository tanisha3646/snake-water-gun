import random
# l=[1,2,3]
# l=["stone","paper","scissor"]
d={
    1:"Snake",
    2:"Gun",
    3:"Water"
}
l=list(d.keys())
chances=10
score=0
q=""
while(True):
    if q!='q':
        if(chances>0):
            choice= int(input("Enter q to quit anytime\nEnter 1 for Snake\nEnter 2 for Gun\nEnter 3 for Water\n"))
            x=random.choice(l)
            if x==choice:
                print("Game tied!Computer chosed ",d[x],"\nYour score is : ",score)
                continue
            elif x>choice:
                score+=1
                print("Congrats!Computer chosed ",d[x],"\nYour score is : ",score)
            elif x<choice:
                score-=1
                print("Oops!Computer chosed",d[x],"\nYour score is : ",score)

        else:
            print("You lose")
    else:
        print("Oops!Game over")