max_attempts=3

for i in range(max_attempts):
    password = input("Enter the password: ")
    if(password == "admin123"):
        print("access granted")
        break
    else:
        print("incorrect password")
else:
    print("Account Locked")
