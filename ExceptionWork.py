try:
    user_input1 = input("Please enter first number: - ")
    user_input2 = input("Please enter second number: - ")

    c = int(user_input1) + int(user_input2)
    print(c)

except:
    print("Your input is incorrect, please enter correct data with only digits")

finally:
    print("This code I want to execute always at the end of code")
