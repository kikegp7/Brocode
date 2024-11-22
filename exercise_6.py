# validate input user exercise

# user is no more than 12 char, not contain spaces and not contain digits

while True:
    username: str = input("Enter your username: ")

    if len(username) > 12:
        print(f"Username {username} must be 12 char max!")
    elif not username.isalpha():
        print(f"Username {username} must contain only alphabetic letters and can't contain spaces!")
    else:
        break

print(f"Your username {username} is valid!. Welcome {username}")
