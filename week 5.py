numbers = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for number in numbers:
    if number>=150:
      break
    elif int(number%5==0):
      print(number) 
    

num = int(input("Guess the number "))
while num < 28:
   print ("guess higher")
   break
else:  
    print("guess lower")

i=0
x=9
while i<10:
    print (i*x)
    i+=1

import random 
list=[]

while len(list)<=10:
    list.append(random.randint(0,100))

print(sum(list)/10)

import random 
list = ["rock", "paper", "scissors"]
player = input("What is your choise? ")
comp = random.choice(list)
if comp == "paper" and player =="rock":
    print ("player wins")
elif comp == "scissors" and player =="rock":
    print ("player wins")
elif comp == "rock" and player =="scissors":
    print ("Computer wins")
elif comp == "rock" and player =="paper":
    print ("Computer wins")
elif comp == "scissors" and player =="paper":
    print ("Computer wins")
elif comp == "paper" and player =="scissors":
    print ("player wins")
elif comp == "paper" and player =="paper":
    print ("it is a tie")
elif comp == "paper" and player =="scissors":
    print ("player wins")
elif comp == "paper" and player =="scissors":
    print ("player wins")
elif comp == "scissors" and player =="scissors":
    print ("it is a tie")
elif comp == "rock" and player == "rock":
    print ("it is a tie")