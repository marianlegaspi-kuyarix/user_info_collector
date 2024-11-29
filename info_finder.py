def search_info(user_name):

    while True:
        find_info = input(user_name).title()

        with open("user_info_collector.txt", "r") as file:
            datas = file.readlines()

        info_devider = ''.join(datas).split("-" * 90)

        for info in info_devider:
            if find_info in info:
                print("\nUSER INFO MATCHED : ")
                print(info.strip())
                return
        print("NO USER INFO MATCHED.")
while True:
     user_name = search_info("Enter full name: ")