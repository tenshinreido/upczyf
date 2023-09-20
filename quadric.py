from math import sqrt
a=float(input('请输入二次项的值'))
b=float(input('请输入一次项的值'))
c=float(input('请输入常数项的值'))

def root(a,b,c):
    if a==0:
        print('x=',c/b)
    elif b**2-4*a*c>=0:
        print('x1=',(-b+sqrt(b**2-4*a*c))/(2*a),'x2=',(-b-sqrt(b**2-4*a*c))/(2*a))
    elif (b**2-4*a*c)==0:
        print('x1=x2=',-b/(2*a))
    else:
        print('no solution in real axis')

def main():
    root(a,b,c)

if __name__=='__main__':
    main()