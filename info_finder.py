#for aesthetic
RESET = "\033[0m"  
BOLD = "\033[1m"  
UNDERLINE = "\033[4m"  
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

print(f"{CYAN}{BOLD}{'-' * 40}WELCOME{'-' * 40}{RESET}")
print(f"{CYAN}{' ' * 35}Information Finder{' ' * 40}{RESET}")
def search_info():

    while True:
        full_name = input(f"{CYAN}{'-' * 87}\nEnter the full name you want to find:{RESET}{YELLOW} ").title()

        if full_name.isdigit():
            print(f"{RESET}{RED}Name cannot be compose of numbers. Please try again.")
        elif len(full_name) <= 3:
            print(f"{RESET}{RED}Name is too short. Please try again.")
        elif not full_name.replace(" ","").isalpha():
            print(f"{RESET}{RED}Name cannot contain non-alpahebetic characters. Please try again.")
        else:
            break
    try:
        with open("user_info_collector.txt", "r") as file:
            datas = file.readlines()
    except FileNotFoundError:
        print("File 'user_info_collector.txt' doesn not exist. Please create it first.")

    info_devider = ''.join(datas).split("-" * 90)

    user_match = False
    for info in info_devider:
        lines = info.strip().split("\n")

        # Ensure the first line contains the name
        if len(lines) > 0:
            name_collected = lines[0].split(" is")[0].strip()  
            if full_name.lower() == name_collected.lower():
                print(f"\n{GREEN}{BOLD}USER INFO MATCHED: {full_name}\n{RESET}")
                print(info.strip())  
                user_match = True
                break

    if not user_match:
        print(f"\n{RED}{BOLD}NO USER INFO MATCHED FOR: {full_name}{RESET}")

while True:
    search_info()
    
    while True:
        continue_search_info = input(f"{CYAN}{'-' * 87}{RESET}\nFind another info? (Yes/No): ").title()
        print(f"{CYAN}{'-' * 87}{RESET}")
        if continue_search_info == "Yes":
            print(f"{GREEN}{BOLD}Searching for another user...")
            break
        elif continue_search_info == "No":
            print(f"{BOLD}{RED}Exiting search...{RESET}")
            break
        else:
            print(f"{RED}Invalid answer. Please answer 'Yes' or 'No'. Try again.{RESET}")
    
    if continue_search_info == "No":
        break

print(f"{CYAN}{BOLD}{'-' * 40}CLOSED{'-' * 40}{RESET}")