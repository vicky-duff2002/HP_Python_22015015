for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("couples", end=", ")
    elif i % 3 == 0:
        print("boys", end=", ")
    elif i % 5 == 0:
        print("girls", end=", ")
    else:
        print(i, end=", ")
