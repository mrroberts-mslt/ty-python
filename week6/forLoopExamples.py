startNumber = int(input("Please enter a start value: "))
endNumber = int(input("Please enter an end value: "))
total = 0

for i in range(startNumber, endNumber+1):
	print("The value of i is:",i)
	total += i
print("Total is :",total)
