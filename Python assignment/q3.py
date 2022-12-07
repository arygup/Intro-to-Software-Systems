a = []
print("enter 10 names with new line charactor as seprator")
for i in range(10):
    val = input()
    a.append(val)
z = int(input("enter any non zero number if you want to sort ascending & zero for descending"))
if(z):
    a.sort()
else:
    a.sort(reverse=True)
print(a)
new = input("please enter another word")
a.append(new)
if(z):
    a.sort()
else:
    a.sort(reverse=True)
print(a)