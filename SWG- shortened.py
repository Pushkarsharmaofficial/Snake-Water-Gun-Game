import random
import pyttsx3
'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([-1, 0, 1])
print('''Choose :
      s for snake 
      w for water
      g for gun''')
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    engine = pyttsx3.init()
    engine.say("Its a draw!!")
    engine.runAndWait()  
    print("Its a draw!!")

else:
    if((computer - you) == -1 or  (computer - you) == 2 ):
        engine = pyttsx3.init()
        engine.say("You lose!!")
        engine.runAndWait()
        print("You lose!!")
    else:
        engine = pyttsx3.init()
        engine.say("You win!!")
        engine.runAndWait()
        print("You win!!") 