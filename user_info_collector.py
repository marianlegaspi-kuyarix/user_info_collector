#Ask for user information
print("USER INFORMATION:")
def valid_name(fullname):
    #loop for the condition
    while True:
        username = input(fullname).title()

        if username.isdigit():
            print("Your name cannot be a number. Please try again.")
        elif not username.isalpha():
            print("Your name cannot contain a non-alpahbetic character. Please try again.")
        elif len(username) <= 2:
            print("Your name must be 3 characters long. Please try again.")
        else:
            return username

def valid_age(age):
    while True:
        user_age =input(age)

        try:
            if user_age.isalpha():
                print("Your age should only be in numeric form. Please try again.")
            elif int(user_age) <= 0 or int(user_age) >= 100:
                print("Invalid age range. Please try again.  ")

            else:
                return user_age
        except ValueError:
            print("Invalid character. Please try again")

def valid_civil_status(status):
    while True:

        civil_status = input(status).title()

        if civil_status.isdigit():
            print("Civil status cannot be a number. Please try again.")
        elif not civil_status.isalpha():
            print("Your civil status can only be either 'Single' or 'Married'. Please choose one of these options. ")
        elif civil_status == "Single":
            return civil_status
        elif civil_status == "Married":
            return civil_status
        else:
            print("Not a valid civil status. Please try again.")

def valid_number(phone):
    while True:
        user_number = input(phone)
        
        if user_number.isdigit():
            if len(user_number) == 11:
                return user_number
            else:
                print("Your phone number must be exactly 11 digits long. Please try again.")
        else:
            print("Your phone number should only contain numeric digits. Please try again.")
            
#loop for the input prompts
while True:
    first_name = valid_name("Enter your first name: ")
    last_name = valid_name("Enter your last name: ")

    print(f"Username: {first_name} {last_name}")

    age = valid_age("How old are you: ")

    print(f"User age: {age}")

    status = valid_civil_status("What is your civil status: ")

    print(f"User civil status: {status}")

    phone = valid_number("Enter your phone number: ")

    print(f"User phone number: {phone}")


