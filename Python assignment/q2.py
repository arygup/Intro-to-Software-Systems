print("enter the number of names")
dat = []
num  = int(input())
for i in range(num):
    a = []  
    roll = int(input("enter roll number"))
    name = input("enter name")
    math = int(input("enter marks in maths"))
    cse = int(input("enter marks in cse"))
    science = int(input("enter marks in science"))
    t = math+science+cse
    a.append(math)
    a.append(science)
    a.append(cse)
    a.sort()
    lis = {"roll number " :  roll, "name " : name, "total score " :  t, "math " : math, "science " : science, "cse " : cse, "mean " : float(t)/3, "median " : a[1] }
    dat.append(lis)
dat = sorted(dat, key = lambda i: i['total score '],reverse=True)
print()
for i in range(num):
    print(dat[i])
print()
search = int(input("enter the roll number of a student who's record you wish to see"))
print()
for i in range(num):
    if(dat[i]["roll number "] == search):
        print(dat[i])
        print("rank = ", i+1)