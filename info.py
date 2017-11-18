users = []

for i in range(3):
    user_info = {"first_name": "", "last_name": ""}
    first_name = input("Введите имя:")
    last_name = input("Введите фамилию:")
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name
    users.append(user_info)
    print(user_info)
print(users)

