"""Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function"""

maxNumber = input("Tell me the size of your odd list: ")
try:
    maxNumber = int(maxNumber)
    oddNumbers = []
    i = 1
    while i <= maxNumber:
        oddNumbers.append(i)
        i+=2
    print(oddNumbers)
except: 
    raise Exception("The size you chose is not an integer")
