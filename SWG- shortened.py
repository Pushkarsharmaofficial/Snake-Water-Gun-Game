import random
import pyttsx3

'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([-1,0,1])
print("Welcome to Snake,Water&Gun Game!!")
n=int(input("Enter the no. of rounds:"))
round= 1
comp=user=0
while round<=n:
  print("Round: ",round)

  print('''Choose :
      s for snake 
      w for water
      g for gun''')
  
  valid_input={'s','w','g'}
  youstr = input("Enter your choice: ").lower()
  
  if youstr in valid_input :
    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if(computer == you):
       engine = pyttsx3.init()
       engine.say("Its a draw!!")
       engine.runAndWait()  
       print("Its a draw!!")
       print("Your score:",user)
       print("Computer score:",comp)

    
    elif((computer - you) == -1 or  (computer - you) == 2 ):
        engine = pyttsx3.init()
        engine.say("You lose!!")
        engine.runAndWait()
        print("You lose!!")
        comp+=1
        print("Your score:",user)
        print("Computer score:",comp)
        round+=1
    else:
        engine = pyttsx3.init()
        engine.say("You win!!")
        engine.runAndWait()
        print("You win!!") 
        user+=1
        print("Your score:",user)
        print("Computer score:",comp)
        round+=1
    
  else:
    print("Invalid input. Please enter valid input.")
  
