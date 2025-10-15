friends = ["Abbas","Kadirov","Rashid"]
adj = ["caliskan", "sap", "belirsiz"]
for sifat in adj:
    for ibne in friends:
        print(sifat, ibne)
for x in "Banana":
    if x == "a":
        continue
    print(x)

for y in range(6):
    if y == 2:
        break
    print(y)
else:
   print("end!")


i = 0
while i < 6:
    i += 1
    print(i)
else:
    print("End")

print("************Carpim tablosu************")
for z in range(1,11):
    for h in range(1,11):
        if (z*h) >= 10:
            print(z*h,end="  ")
        else:
            print(z*h,end="   ")
    print()
print("************Carpim tablosu**************")
    
    