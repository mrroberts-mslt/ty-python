stars=int(input("enter stars: "))
output = stars-1
for row in range(stars):
    for col in range(stars):        
        if (row == 0 and col< output) or (row < output and col == 0) or (row < output and col == output) or (row == output and col <= output):
            print("*",end="")
        else:
            print(end=" ")
    print()

print("You legend!!")
for row in range(6):
    for col in range(7):
        if (row ==0 and col%3!= 0) or (row == 1 and col%3 == 0) or (row-col == 2) or (row + col == 8):
            print("*",end="")
        else:
            print(end=" ")
    print()
