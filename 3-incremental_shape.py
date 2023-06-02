# program to print the # shape incrementally

valid_input = False

while not valid_input:

    user_input = input("Enter an integer: ")

    if user_input.isdigit():

        valid_input = True

    else:

        print("Only integer characters are allowed, try again.")

num = int(user_input)

for i in range(1, num+1):

    print("#" * i)
