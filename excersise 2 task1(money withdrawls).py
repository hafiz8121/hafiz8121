balance = 1000
print("your balance is", balance, "sek")
user_input = int(input("how much money do you want to withdraw(in 100's): "))

if user_input <= balance:
    balance -= user_input
    print("you have withdrawn", user_input, "sek")
    print("your new balance is", balance, "sek")