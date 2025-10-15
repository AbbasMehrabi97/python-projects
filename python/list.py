myList = ["banana", "Apple","Orange"]
print(len(myList))
print(type(myList))
myList[1] = "Cherry"
myList.insert(2,"Pineapple")
if "Apple" in myList:
    print("Yes")
print(myList)
newlist = myList.copy()
print(newlist)
list2 = list(newlist)
print(list2)  