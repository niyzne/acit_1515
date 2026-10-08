login = {"username": "sarah123", "password": "apple123"}

for attempt in range(3):
    password = input(f"Enter a password for {login['username']}")
    if password == login["password"]:
        print(f"you typed {password}")
        break
else:
    print("Please type it right next time")
