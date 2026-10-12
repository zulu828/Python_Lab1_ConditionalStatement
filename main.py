import BMI
import zodiac
import birthday_guess

while True:
    print("Select 'a1' -> BMI Calculation")
    print("Select 'a2' -> Zodiac Finder")
    print("Select 'a3' -> Birthday Predictor")
    print("Select 'a4' -> Exit Program")
    
    user_choice = input("Select an option: ")
    
    if user_choice == "a1":
        BMI.zulu()
    elif user_choice == "a2":
        zodiac.zulu()
    elif user_choice == "a3":
        birthday_guess.zulu()
    elif user_choice == "a4":
        break