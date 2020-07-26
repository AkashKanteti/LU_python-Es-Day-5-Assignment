list1=[5,15,25,35,45,60]
list2=[10,20,40,60,70,80]
list3=list1+list2
len=len(list3)
for i in range(len):
    mi=min(list3[i:])
    if list3[i]>mi:
        print(mi)
        temp=list3[i]
        index=i+list3[i:].index(list3[i])
        index1=i+list3[i:].index(mi)
        list3[index]=mi
        list3[index1]=temp
print(list3)
