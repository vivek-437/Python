import random 
lst = ["s","g","w"]
chance = 10
print("You will get only ten chance")
number_of_chance = 0
your_point=0
opponent_point=0
while number_of_chance<chance:
    _input = input("sanke,gun,water:-\n")
    r = random.choice(lst)
# while user input is "s"
    if _input.lower()==r:
        print("Bhai doono mein se koi nahi jeeta\n")
        number_of_chance=number_of_chance+1
    elif _input.lower()=="s" and r=="g":
        opponent_point=opponent_point+1
        print("Bhai aapko gun ne udda diya")
        number_of_chance=number_of_chance+1
        print("You loss")
        print(f"you choose {_input} and opponent choose {r}")
        print(f"your point {your_point} and opponent point {opponent_point}")
    elif _input.lower()=="s" and r=="w":
        your_point=your_point+1
        number_of_chance=number_of_chance+1
        print("Bahi aap ne toh pani peeliya\n")
        print("You win")
        print(f"you choose {_input} and opponent choose  {r}")
        print(f"your point {your_point} and opponent point {opponent_point}")
# while  user input is g 
    elif _input.lower()=="g" and r=="s":
        your_point=your_point+1
        number_of_chance=number_of_chance+1
        print("aapne gun se snake ko maar diya\n")
        print("you win")
        print(f"you choose {_input} and opponent choose {r}")
        print(f"your point {your_point} and opponent point {opponent_point}")
    elif _input.lower()=="g" and r=="w":
        opponent_point=opponent_point+1
        number_of_chance=number_of_chance+1
        print("Bhai gun toh pani me doobgayi")
        print("You loss")
        print(f"you choose {_input} and opponent choose{r}")
        print(f"your point {your_point} and opponent point {opponent_point}")
# while  user input is w
    elif _input.lower()=="w" and r=="s":
        number_of_chance=number_of_chance+1
        opponent_point=opponent_point+1
        print("Bhai snake ne toh pani peeliya\n")
        print("You loss")
        print(f"you choose {_input} and opponent choose {r}")
        print(f"your point {your_point} and opponent point {opponent_point}")
    elif _input.lower()=="w" and r=="g":
        your_point=your_point+1
        number_of_chance=number_of_chance+1
        print("Bhai aapne gun ko doobadiya\n")
        print("you win")
        print(f"you choose {_input} and opponent choose {r}")
        print(f"your point {your_point} and opponent point {opponent_point}")
    else:
        print("Type the correct character") 

print("Game Over")

if your_point<opponent_point:
    print("You loss the match ")
    print(f"your total point is {your_point} and opponenet point is {opponent_point}")

elif opponent_point<your_point:
    print("You win the match ")
    print(f"your total point is {your_point} and opponenet point is {opponent_point}")

else:
    print("Both are the winners")
    print(f"your total point is {your_point} and opponenet point is {opponent_point}")


        