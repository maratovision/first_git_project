def register(username, password, check_password):
    if password == check_password:
        if 8 < len(username) < 40 and 8 < len(password) < 16:
            print("Успешно")
            with open("database.txt", "w") as db1:
                db1.write(username + '\n' + password)
                code = 1234
                return code
        else:
            print("Неправильная длина")
    else:
        print("Пароли не совпадают")

register("testname123", "password123", "password123")