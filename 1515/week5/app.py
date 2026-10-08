login = {"Username": "sarah123", "password": "apple123"}

while True:
    password = input(f"Enter a password for {login['username']}")
    if password == login["password"]:
        print(f"you typed {password}")
        break
