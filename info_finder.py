def search_info(full_name):

    while True:
        find_info = input(full_name).title()

        if len(find_info) <= 3:
            print("Name is too short. Please try again.")
        elif not find_info.replace(" ","").isalpha():
            print("Name cannot contain non-alpahebetic characters. Please try again.")
        else:
            search_info(full_name)
        with open("user_info_collector.txt", "r") as file:
            datas = file.readlines()

        info_devider = ''.join(datas).split("-" * 90)

        for info in info_devider:
            if full_name in info:
                print("\nUSER INFO MATCHED : \n")
                print(info.strip())
                return
        print("NO USER INFO MATCHED.")
while True:
     first_name = search_info("Enter full name: ")
     


