print("Hello, World!")
x = 5
y = "John"
print(x)
print(y)
x = str(3)
y = int(3)
z = float(3)
x, y, z = "Zabet", "Shamsuddin", "Shapur"
x = y = z = "Abbas"
fruits = ["Apple", "Orange", "Banana"]
x, y, z = fruits
print(x)
print(y)
print(z)
print(x, y, z)
print(x + y + z)
print(type(x))
print(type(y))
print(type(z))
x = "awesome"
def myfunc():
    global x 
    x = "fantastic"
    print("python is " + x)
myfunc()

print("python is " + x)

x = range(6)
print(x)
x = {"name" : "Abbas","age" : 28}
print(x)
name = input("Enter your name: ")
print("Hello", name)