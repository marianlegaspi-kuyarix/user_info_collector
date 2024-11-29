def search_info():

    while True:
        full_name = input("Enter the full name you want to find: ").title()

        if full_name.isdigit():
            print("Name cannot be compose of numbers. Please try again.")
        elif len(full_name) <= 3:
            print("Name is too short. Please try again.")
        elif not full_name.replace(" ","").isalpha():
            print("Name cannot contain non-alpahebetic characters. Please try again.")
        else:
            break

    with open("user_info_collector.txt", "r") as file:
        datas = file.readlines()

    info_devider = ''.join(datas).split("-" * 90)

    user_match = False
    for info in info_devider:

        lines = info.strip().split("\n")
        if len(lines) > 2:
            name_line = lines[2].strip()
            if full_name in name_line:
                print("\nUSER INFO MATCHED : \n")
                print(info.strip())
                user_match = True
                break
    if not user_match:
        print("NO USER INFO MATCHED.")
        print(lines)
while True:
    search_info()
    

