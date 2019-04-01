limit = int(input("Enter the limit: "))
myList = []
for i in range(0,limit):
    element = int(input("Enter the element: "))
    myList.append(element)
print([x for x in myList if x >= 5])
