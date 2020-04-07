# ATM word
CONST_PIN = 1234
enter_pin = int(input("Enter pin: ")) 
if  enter_pin == CONST_PIN:
    print("Yes, YOU ARE RIGHT")
else:
    print("No, WHAT A SORE LOOSER!")


CONST_OPTIONS = ("withdraw")
enter_options = input("ENTER YOUR OPTION:  ")
if enter_options == CONST_OPTIONS:
    print("YES, YOU ARE CORRECT")
else:
    print("NO, GIVE IT ANOTHER TRY")

account_type = ("savings, current")
enter_options = input("select_account:  ")
if enter_options in account_type:
    print("Yes, good work")
else:
    print("No, try again")


amount = (1000, 2000, 5000, 10000)
amount = int(input("Enter amount: "))
if amount <= 10000:
    print("Nice work")
else:
    print("try again")
if amount >= 10000:
    amount = int(input("Enter amount: "))
    print("Good")


print("dispense cash")
