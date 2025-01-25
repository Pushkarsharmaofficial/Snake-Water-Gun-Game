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
    if(computer ==-1 and you == 1): 
        engine = pyttsx3.init()
        engine.say("You win!!")
        engine.runAndWait()
        print("You win!!")

    elif(computer ==-1 and you == 0):
        engine = pyttsx3.init()
        engine.say("You lose!!")
        engine.runAndWait()
        print("You lose!!")
    

    elif(computer == 1 and you == -1):
        engine = pyttsx3.init()
        engine.say("You lose!!")
        engine.runAndWait()
        print("You lose!!")
        

    elif(computer ==1 and you == 0):
        engine = pyttsx3.init()
        engine.say("You win!!")
        engine.runAndWait()
        print("You win!!")

    elif(computer ==0 and you == -1):
        engine = pyttsx3.init()
        engine.say("You win!!")
        engine.runAndWait()
        print("You win!!")

    elif(computer == 0 and you == 1):
        engine = pyttsx3.init()
        engine.say("You lose!!")
        engine.runAndWait()
        print("You lose!!")


    else:
        print("Something went wrong!")