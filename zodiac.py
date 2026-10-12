def zulu():
    birth_year = int(input("Eneter your brith year",))
    zodiac = birth_year%12
    if zodiac==0:
        z="Monkey"
    elif zodiac==1:
        z="Rooster"
    elif zodiac==2:
        z="Dog"
    elif zodiac==3:
        z="Pig"
    elif zodiac==4:
        z="Rat"
    elif zodiac==5:
        z="Ox"
    elif zodiac==6:
        z="Tiger"
    elif zodiac==7:
        z="Rabbit"
    elif zodiac==8:
        z="Dragon"
    elif zodiac==9:
        z="Snake"
    elif zodiac==10:
        z="Horse"
    else:
        z="Sheep"
    print("Your zodiac sign is:",z)