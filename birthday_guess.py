def zulu():
    set_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    set_2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31]
    set_4 = [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31]
    set_8 = [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31]
    set_16 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    
    number_groups = [set_1, set_2, set_4, set_8, set_16]
    calculated_day = 0 
    
    for index in range(5):
        print("Set", index + 1, ":", number_groups[index])
        print("Is your birthday included in this set?")
        user_response = int(input("Enter 1 for Yes and 0 for No: "))
    
        if user_response == 1:
            calculated_day += number_groups[index][0] 
    
    print("Your birthday is:", calculated_day)