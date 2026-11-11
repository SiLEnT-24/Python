# while True:
#     print("hellooo")             # this print infinite helloooo

correct_password = "python"
while True:
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("Access granted")
        break   
    else:
        print("Access denied. Try again.")

print("logged in")