def register(username, password, check_password):
    # "Пароль начинается с заглавной буквы, состоит из цифр и букв, длина больше 10 символов"
    # Validate password
    if password.istitle() and not password.isdigit() and not password.isalpha() and len(password) > 10:
        if password == check_password:
            print("Регистрация")
        else:
            print("Пароли не совпадают")
    else:
        print("Соблюдайте правила")
username = input("Введите имя: ")
password = (input("Введите пароль: "))
check_password = (input("Подтвердите пароль: "))

register(username, password, check_password)