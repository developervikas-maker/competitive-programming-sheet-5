mylist = [1.4, 2, 3, 4, 5, "bharat"]
rev = []
for i in range(len(mylist)-1, -1, -1):
    rev.append(mylist[i])
print(rev)