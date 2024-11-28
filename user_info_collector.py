#Ask for user info 
print("User information.")
while True:
        first_name = input("Enter your first name: ").title()
        if first_name.isdigit():
            print("Your name cannot be a number")    
        elif len(first_name) <= 2:
            print("Are you sure your entered your first name correctly?")
            continue
        last_name = input("Enter your last name: ").title()
        if last_name.isdigit():
            print("Your name cannot be a number")
        if len(last_name) <= 2:
         print("Are you sure your entered your last name correctly?")
         continue
        print(f"{first_name} {last_name}")