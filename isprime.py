from math import sqrt
#输出从3到n的所有素数
n = input("请输入判断范围")
primelist = []
for i in range(2, int(n)):
    flag = 1
    for factor in range(2, int(sqrt(i))+1):
        if i % factor == 0:
            flag = 0
            break
    if flag == 1:
        primelist.append(i)
print(primelist)