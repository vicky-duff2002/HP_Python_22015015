vi = input("Enter a letter: ")
if ord(vi) >= 65 and ord(vi) <= 90:
    print(vi, "is an uppercase letter.")
elif ord(vi) >= 97 and ord(vi) <= 122:
    print(vi, "is lowercase letter.")
else:
    print(vi, "is not a letter.")
