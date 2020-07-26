li=[1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
li.sort()
i=0
while True:
    if li[i]==0:
        li.append(li.pop(i))
    else:
        break
print(li)
