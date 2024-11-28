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
            elif 0 >= int(user_age) >= 100:
                print("Invalid age range. Please try again.  ")
            else:
                return user_age
        except ValueError:
            print("Invalid character. Please try again")
#loop for the input prompts
while True:
    first_name = valid_name("Enter your first name: ")
    last_name = valid_name("Enter your last name: ")

    print(f"Username: {first_name} {last_name}")

    age = valid_age("How old are you: ")

    print(f"User age is {age}")

