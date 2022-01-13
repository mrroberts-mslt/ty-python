answer = input("Should I keep going? Y / N")
while answer == Y:
  answer = input("Should I keep going? Y / N")
  
#Loop example 1
while True:
     print("This goes on forever")

#Loop example 2    
counter = 0
while counter <=10:
    print("*" * counter)
    counter +=1
    
#Loop example 3 
startNum = int(input("Enter a start number: "))
endNum = int(input("Enter a end number: "))

counter = startNum
total = 0
while counter <= endNum:
    print(counter)
    counter +=1
    total += counter
print("The total is: ",total)

#Loop example 4 
myLetter = input("Enter a letter: ")

while myLetter != "z":
    print("Letter entered is", myLetter)
    myLetter = input("Enter a letter: ")
print("finished")
