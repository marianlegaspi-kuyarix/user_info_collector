def search_info():

    while True:
        full_name = input(f"Enter the full name you want to find: ").title()

        if full_name.isdigit():
            print("Name cannot be compose of numbers. Please try again.")
        elif len(full_name) <= 3:
            print("Name is too short. Please try again.")
        elif not full_name.replace(" ","").isalpha():
            print("Name cannot contain non-alpahebetic characters. Please try again.")
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
        if len(lines) > 0 and full_name in lines[0]:
            print(f"\nUSER INFO MATCHED : {full_name}\n")
            print(info.strip())
            user_match = True
            break

    if not user_match:
        print("NO USER INFO MATCHED.")

while True:
    search_info()

    continue_search_info = input(f"\nFind another info? (Yes/No): ").title
    if continue_search_info == "Yes":
        search_again = input("Enter the full name you want to find: ")
        if search_again.isdigit:
            print("Name cannot be compose of numbers. Please try again.")
        elif len(search_again) <= 3:
            print("You entered a name too short. Please try again.")
        elif not search_again.replace(" ","").isalpha():
            print("Name cannot contain non-alpahebetic characters. Please try again.")
        else:
            continue
        

