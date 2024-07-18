def indexofguess(x):
    return i


print("""__        __   _                            _          _   _                
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___       
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \      
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/      
 _ \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/__ \__|_| |_|\___|      
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __    / ___| __ _ _ __ ___   ___ 
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | |  _ / _` | '_ ` _ \ / _ \\
|  _  | (_| | | | | (_| | | | | | | (_| | | | | | |_| | (_| | | | | | |  __/
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  \____|\__,_|_| |_| |_|\___""")
print("       YOU HAVE 7 LIVES    ")
list1=["apple","mango","pineapple","kiwi","banana","orange"]

import random
chosenword=random.choice(list1)

print(f"  ##  HINT :   ITS A FRUIT   OF {len(chosenword)}   letters ==  '{"_ "*len(chosenword)}' ")

spaces=""
for i in range(0,len(chosenword)):
    spaces+="_"

listofspaces=list(spaces)
print("".join(listofspaces))

p=0
lifeused=0
finalanswer=""


while 5>0:


    guess=input("Enter a character which you think is present in the world   :  ")

    if guess in chosenword:
        print(f"You guessed right ''{guess}'' is present in the word ")
        for i in range(0,len(chosenword)):
            if chosenword[i]==guess:
                p=indexofguess(i)
                listofspaces[p]=guess
        for n in listofspaces:
            print(n,end=" ")
        print("\n")      
        finalanswer="".join(listofspaces)

        if finalanswer==chosenword:
            print("<<<   woooo hoooo You won   >>>   ")
            break
        else:
            continue

        

    else:
        lifeused+=1
        print("   ####           you lose a life          ####  ")
        
        if lifeused==1:
            print("""  +---+
      |   |
          |
          |
          |
          |
    =========""")
            print("Now only 6 lives are left ")
        elif lifeused==2:
            print("""  +---+
      |   |
      O   |
          |
          |
          |
    =========""")
            print("Now only 5 lives are left ")
            
        elif lifeused==3:
            print("""  +---+
      |   |
      O   |
      |   |
          |
          |
    =========""")
            print("Now only 4 lives are left ")
        elif lifeused==4:
            print("""  +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""")
            print("Now only 3 lives are left ")
        elif lifeused==5:
            print("""  +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========""")
            print("Now only 2 lives are left ")
        elif lifeused==6:
            print("""  +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========""")
            print("Now only 1 lives are left ")
        elif lifeused==7:
            print("""  +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========""")
            
            
            print("                <<< AAPKA KHEL SAMAPT HUA AAP HAAR CHUKE HO >>>")
            break
        
print(finalanswer)
               

