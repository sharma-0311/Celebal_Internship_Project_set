rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(rows):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
