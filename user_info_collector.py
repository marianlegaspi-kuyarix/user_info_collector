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

def valid_gender(gender):
    while True:
        user_gender = input(gender).title()

        if not user_gender.isalpha():
            print("Your Gender is not amongst the available options. Please try again.")
        elif user_gender == "Female":
            return user_gender
        elif user_gender == "Male":
            return user_gender
        elif user_gender == "Other":
            
            while True:
                other = input("Are you perhaps Nonbinary or Genderfluid? (Yes/No): ").title() 
                if other == "Yes":
                    yes_other = input("Can you specify your gender (Nonbinary/Genderfluid): ").title()
                    if yes_other in ["Nonbinary", "Genderfluid"]:
                            return yes_other
                    if not yes_other.isalpha():
                        print("Your Gender is not amongst the available options. Please try again.")
                    else:
                        print("Invalid input. Please specify 'Nonbinary' or 'Genderfluid'.")
                elif other == "No":
                    return "and did not specify their gender"
                else:
                    print("Not a valid response. Please answer 'Yes' or 'No'.")
                    
        else:
            print("Not a valid gender. Please try again.")

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

def valid_hometown(town):
    while True:
        user_town = input(town).title()

        if user_town.isdigit():
            print("Your hometown cannot be a number. Please try again.")
        elif not user_town.isalpha:
            print("Your hometown cannot cointain any non-alaphabetic characters. Please try again.")
        elif len(user_town) <= 4:
            print("Not a valid town name. Please try again.")
        else:
            return user_town

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

def most_important_question(arcane):
    while True:
        important = input(arcane).title()

        if important == "Yes":
            while True:
                caitvi = input("This is the most important question! \nDO YOU LIKE CAITLYN AND VI (YES/NO): ").upper()
                if caitvi == "YES":
                    return "YOU ARE THE GOAT, CAITVI IS THE BEST. LESBIANS LET'S GO!"
                elif caitvi == "NO":
                    return "I HOPE BOTH YOUR PILLOWS ARE WARM!"
                elif not caitvi.isalpha():
                    print("Answer the damn QUESTION! YES OR NO.")
                else:
                    print("Answer the damn QUESTION! YES OR NO.")
        elif not important.isalpha():
            print("That is not a valid answer! Please try again.")
        elif important == "No":
            return "Oh! You should watch it some other time. You would like it."
        else:
            print("That is not a valid answer! Please try again.")

#list of dictionary for users data/info
collected_data = []  
                                  
#loop for the input prompts
while True:

    user_info = {}
    user_info["first_name"] = valid_name("Enter your first name: ")
    user_info["last_name"] = valid_name("Enter your last name: ")
    user_info["gender"] = valid_gender("What is your gender? (Male/Female/Other): ")
    user_info["age"] = valid_age("How old are you: ")
    user_info["status"] = valid_civil_status("What is your civil status? (Single/Married): ")
    user_info["town"] = valid_hometown("Where is your hometown: ")
    user_info["phone"] = valid_number("Enter your phone number: ")
    user_info["arcane"] =  most_important_question("For the last requirement.\nHave you watched Arcane? (Yes/no): ")

    collected_data.append(user_info)

    another_entry = input("Do you want to add another entry? (Yes/No): ").title()
    if not another_entry.isalpha():
        print("Invalid response. Please try again.")
    elif another_entry == "Yes":
        print("NEW USER INFORMATION")
        continue
    elif another_entry == "No":
        print("Exiting...collecting of data..")
        break
    else:
        print("Invalid response. Please try again.")

#saving data into txt fle
with open("user_info_collector.txt", "a") as file:
    
    for data in collected_data:
        file.write(f"""{'-'*90}
USER INFORMATION
{'-'*90}
{data["first_name"]} {data["last_name"]} is a {data["age"]} years old {data["gender"]}.
They are from {data["town"]} and currently {data["status"]}.
To reach them, their phone number is {data["phone"]}.
When ask about arcane best ship, the interviewer could not contain themselves and said;\n{data["arcane"]}.\n
{'-'*90}\n\n""")
print("User information has been saved to 'user_info_collector.txt'")