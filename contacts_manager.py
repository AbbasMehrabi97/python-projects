contacts = {}
try:
    with open("names.txt", "r") as f:
        for line in f:
            name, number = line.strip().split(" : ")
            contacts[name] = number
except FileNotFoundError:
    pass

while True:
    action = input("enter a to add d to delete s for search x for saving e to exit = ").lower()
    match action:
        case "a":
            name, number = input("Please insert the  name and number = ").split()
            contacts[name] = number
        case "d":
            delname = input("Please insert the  name you want ot delete = ")
            if delname in contacts:
                contacts.pop(delname)
                print(f"{delname} deleted")
            else:
                print("Name not found")
        case "s":
            serch_name = input("Please insert the name you want ot search = ")
            if serch_name in contacts:
                print(serch_name , ":", contacts[serch_name])
            else:
                print("Not found")
        case "x":
            with open("names.txt", "w") as f:
                for name, number in contacts.items():
                    f.write(name + " : " + number + "\n")
            print("Contacts saved")
        case "e":
            break
        case _:
            print("try again")