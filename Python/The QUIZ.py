#Hi! This is a new project.My first one :).
#My name is : ADVAIT
#All the comments in this code will be for my understanding and future refrence.
#This project is inspired from @Tech with TIm(YT)...
#Inspired from his video but coded with the leeast help possible...Lets GO!
#-------------------------------------------------------------------------------

#This will be the intro of the game.

Start = input("Are you ready for the QUIZ?")

#The First mistake : after ".lower" or anything after "." always put "()".

if Start.lower()!= "yes":
     quit()

print ("Let's Begin!")
score = 0


key = input("Who wrote this code?")
if key.lower() == "advait" :
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")
#This was a successssssssss!!!!

key = input("What is the best Programming Language?")
if key.lower() == "python" :
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

key = input("What is the Capital of India?")
if key.lower() == "delhi" :
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

key = input("What is the fifth prime number? (use text only)")
if key.lower() == "eleven" :
    print("CORRECT!")
    score += 1
else:
    print("INCORRECT!")

print ("Your got "+ str(score) + " Correct")
print ( " Your precentage: " + str((score/4) * 100) + "%" )

if score < 1 :
    print("You Gotta Study Child")
elif score == 1:
    print ("AVERAGE")
elif score == 2 :
    print ("Can do Better!")
elif score == 3:
    print ("Good Job! Next Time Hit The Bounty :).")
else:
    print("Excellent Performance! Now Prepare for the next Test or You are Grounded!!")

#Finished my firt PROJECT :).
