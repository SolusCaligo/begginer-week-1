acc_pin = int(input("enter your account pin:"))
if acc_pin == 1234:
    print("you can access your account")

    credit = int(input("Enter the amount to credit: "))

    if credit < 580:
        print("you naughty, you can't credit less than 580")

    elif credit >= 580 and credit < 670:
        print("you ok I guess")

    elif credit >= 670:
        print("you a good boy, you can credit more than 670")

else:
    print("you can't access your account, wrong pin")
