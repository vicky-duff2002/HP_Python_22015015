try:
    num = int(input("Enter an odd number: "))
    if num % 2 == 0:
        raise ValueError
    else:
        for i in range(num, 0, -2):
            for j in range(int((num-i)/2)):
                print(" ", end="")
            for j in range(i):
                print("*", end=" ")
            print()
except ValueError:
    print("Input must be an odd number.")
