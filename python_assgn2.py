#********Answer 1******************
x='Python is a case sensitive language'

print(len(x))                                            #part a  

print(x[::-1])                                           #part b         

y=slice(10, 27)                                          #part c         
NewX=x[y]
print(NewX)

print(x.replace('a case sensitive', 'object oriented'))  #part d        

print(x.index('a'))                                      #part e       

print(x.replace(' ', ''))                                #part f


print()
print()

#******Answer 2********************
name=input('Enter your name: ')
SID=int(input('Enter your SID: '))
Dep=input('Enter your department: ')
CGPA=int(input('Enter your CGPA: '))
print('Hey, ',name,' Here!\nMy SID is',SID,'\nI am from ',Dep,' department and my cgpa is',CGPA)

print()
print()

#******Answer 3*******************
a=56
b=10

print(a&b)
print(a|b)
print(a^b)
print(a<<2, b<<2)
print(a>>2, b>>4)

print()
print()

#********Answer 4*****************
Num1=int(input('Enter number 1:'))
Num2=int(input('Enter number 2:'))
Num3=int(input('Enter number 3:'))
if Num1>=Num2 and Num1>=Num3:
    print('Greatest number is:',Num1 )
elif Num2>=Num1 and Num2>=Num3:
    print('Greatest number is:',Num2 )
else:
    print('Greatest number is:',Num3 )

print()
print()

#********Answer 5******************
user=input('Enter any string: ')
if 'name' in user:
    print('yes')
else:
    print('no')

print()
print()

#******Answer 6********************
side1=int(input('Enter the length of side 1: '))
side2=int(input('Enter the length of side 2: '))
side3=int(input('Enter the length of side 3: '))
if side1>side2+side3 and side2>side1+side3 and side3>side2+side1:
    print('yes')
else:
    print('no')
  







