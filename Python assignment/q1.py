val = int(input("Enter your value: "))

for i in range(int(val),1,-2):
    for k in range(val - i):
        print("", end = " ")
    for j in range(i):
        print("*", end =" ")
    print()
for i in range(2,int(val)+2,2):
    for k in range(val - i):
        print("", end = " ")
    for j in range(i):
        print("*", end =" ")
    print()



#print(val) 