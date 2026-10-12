def zulu():
    weight = int(input("Enter your weight (kg): ",))
    height = float(input("Enter your height (m): ",))
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        print("you are Underweight")
    elif 18.5 <= bmi <= 24.9:
        print("you are Normal weight")
    elif 25.0 <= bmi <= 29.9:
        print("you are Overweight")
    else:
        print("you are Obese")