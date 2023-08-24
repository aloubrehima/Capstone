import datetime

name = input("What's your name? ")
birthday_month = input("What month were you born in? ")

print(f"Hello, {name}!")

current_month = datetime.datetime.now().strftime("%B").lower()

if birthday_month.lower() == current_month:
    print("Happy birthday month!")

name_len = len(name)
print(f"There are {name_len} letters in your name.")



