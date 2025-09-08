user=str(input("Enter your username:"))
# print(type(user))
if not user.isalpha():
    raise ValueError('Enter only A-Z')
else:
    print("Registration Successfully")

print(user)