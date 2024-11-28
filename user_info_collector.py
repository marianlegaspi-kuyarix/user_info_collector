#Ask for user information
print("User information.")
while True:
        #Ask for user first name
        first_name = input("Enter your first name: ").title()
        if first_name.isdigit():
            print("Your name cannot be a number") 
        elif not first_name.isalpha():
            print("Your name cannot contain a non alpahbet character.")
        elif len(first_name) <= 2:
            print("Are you sure your entered your first name correctly?")
        #ask for user last name
        last_name = input("Enter your last name: ").title()
        if last_name.isdigit():
            print("Your name cannot be a number")
        elif not last_name.isalpha():
            print("Your name cannot contain a non alpahbet character.")
        if len(last_name) <= 2:
            print("Are you sure your entered your last name correctly?")
        print(f"{first_name} {last_name}")