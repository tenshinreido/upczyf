arr=input("请输入数组")
lst=[int(n) for n in arr.split()]
for i in range(0,len(lst)-1):
    for j in range(0,len(lst)-1-i):
        if lst[j]<lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]

print(lst)