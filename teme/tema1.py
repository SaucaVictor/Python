x=input("1. x= ")
x=int(x)
print(5*x,)

y=float(input("2. y= "))
z=float(input("   z= "))
print(y*z,)

a=int(input("3. a= "))
b=int(input("   b= "))
print("cat: "+str(a//b)+" rest: "+str(a%b),)

c=int(input("4. c= "))
d=int(input("   d= "))
print("+: "+str(c+d)+" ; -: "+str(c-d)+" ; *: "+str(c*d)+" ; /: "+str(c//d),)

e=int(input("5. e= "))
for i in range(11):
    print(str(i)+" * "+str(e)+" = "+str(i*e),)

f=input("6. f= ")
g=input("   g= ")
print((f+g)+" "+(g+f),)

print("7.\n",end='')
for i in range(9):
    print("*",end='')
print("\n* "+"@",end='')
for i in range (3):
    print(" ",end='')
print("@"+" "+"*","\n*",end='')
for i in range (3):
    print(" ",end='')
print("*",end='')
for i in range (3):
    print(" ",end='')
print("*\n",end='')
print("*"+" "+" "+"\_"+"/"+" "+" "+"*",)
for i in range(9):
    print("*",end='')

print("\n")
n=int(input("8. n= "))
print(str(n)+"^2 = "+str(n**2)+", "+str(n)+"^3 = "+str(n**3))

