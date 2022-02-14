print('***********************Answer 1***********************')
print()

#***********************Answer 1***********************

def Occurrence(str):                   #function find occ. of words
    occurrence=dict()
    words=str.split()
    for i in words:
        if i in occurrence:
            occurrence[i]+=1
        else:
            occurrence[i]=1
    return occurrence
def CharaOccurrence(str):              # function to find occ. of characters
    occurrence=dict()
    for i in str:
        if i in occurrence:
            occurrence[i]+=1
        else:
            occurrence[i]=1
    return occurrence
str=input('Enter your string: ')
x=str.split()
if len(x)==1:                          #using len() to divide beteween single word and line
    print(CharaOccurrence(str))
else:
    print(Occurrence(str))

print()
print()
print('***********************Answer 2***********************')
print()
print()

#***********************Answer 2***********************

def leapyear(year):              #function for year year
    leap = False
    if year%400==0 :
        leap = True
    elif year%4 == 0 and year%100 != 0:
        leap = True
    return leap
day=int(input('Day-'))
month=int(input('month-'))
year=int(input('year-'))

if day<31 and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):   #months with 31 days
    print('Next day is ', (day+1), '/', month, '/', year)  

elif day==31 and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10):
    print('Next day is ', 1, '/', month+1, '/', year)

elif month==2 and day<28:                                                                             #febuary 
    print('Next day is ', day+1, '/', month, '/', year)

elif month==2 and day==28 and leapyear(year)==True:
    print('Next day is ', 29, '/', month, '/', year)

elif month==2 and day==29 and leapyear(year)==True:
     print('Next day is ', 1, '/', month+1, '/', year)

elif month==2 and day==28 and leapyear(year)==False:
    print('Next day is ', 1, '/', month+1, '/', year)

elif day<30 and (month==4 or month==6 or month==9 or month==11):                                      #months with 30 days
    print('Next day is ', day+1, '/', month, '/', year)

elif day==30 and (month==4 or month==6 or month==9 or month==11):
    print('Next day is ', 1, '/', month+1, '/', year)

elif day==31 and month==12:                                                                           #31st december
    print('Next day is ', 1, '/', 1, '/', year+1)

else:
    print('The user has entered incorrect date.')



print()
print()
print('***********************Answer 3***********************')
print()
print()

#***********************Answer 3***********************

def square(lst):                             #crating a function
    sq=[]
    for i in range(0,len(lst)):
        a=[(lst[i],lst[i]**2)]
        sq.append(a)
        i+=1
    return sq
lst=()                                       #creating a tupple
n=int(input('Enter number of terms:'))
for i in range(0,n):                                               
    z=int(input('Enter numbers:'))          
    lst=lst+(z,)          
    i+=1
print(square(lst))     


print()
print()
print('***********************Answer 4***********************')
print()
print()

#***********************Answer 4***********************

grade=int(input('Enter the grade:'))
if grade==10:                                #using if-elif to define Lgrade and performance
    Lgrade='A+'
    performance='Outstanding'
elif grade==9:
    Lgrade='A'
    performance='Excellent'
elif grade==8:
    Lgrade='B+'
    performance='Very Good'
elif grade==7:
    Lgrade='B'
    performance='Good' 
elif grade==6:
    Lgrade='C+'
    performance='Average'
elif grade==5:
    Lgrade='C'
    performance='Below Average'
elif grade==4:
    Lgrade='D'
    performance='Poor'
print(f'Your Grade is {Lgrade} and {performance} Performance')

print()
print()
print('***********************Answer 5***********************')
print()
print()

#***********************Answer 5***********************

n = 6

for i in range(n):
    
    for j in range(i):
        print(' ', end='')
    
    for j in range(((n-i)*2)-1):
        print(chr(65 + j), end='')
    print()

print()
print()
print('***********************Answer 6***********************')
print()
print()

#***********************Answer 6***********************

def dict(d):                                                                                   #function to take input
    key = int(input("Enter the SID:"))
    value = input("Enter the name:")
    d[key] = value

student_details = {}

ans = 'y'
while ans == 'y':
    dict(student_details)

    ques = input("\nDo you want to enter another value?[y/n]:")

    if ques == 'y':
        ans = 'y'
    elif ques == 'n':
        break
    else:
        print("Error! Only y/n should be entered.")
        exit()

print('SID\t\tNames')                                                                             #part A
for k in student_details:
    print(f"{k}\t\t{student_details[k]}")

dict_sortedbynames = {k: v for k, v in sorted(student_details.items(), key=lambda v: v[1])}       #part B
print(dict_sortedbynames)

dict_sortedbySID = {k: v for k, v in sorted(student_details.items())}                             #part C
print(dict_sortedbySID)

f = int(input("\nEnter the SID which you want to search:"))                                       #part D

if f in student_details.keys():
    print(f"Name of student with SID {f} is: \"{student_details[f]}\"")
else:
    print(f"Error! {f} not found.")


print()
print()
print('***********************Answer 7***********************')
print()
print()

#***********************Answer 7***********************

def Fibonacci(n):                                      #function to create fibonacci series
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
n=int(input('Number of terms of fibonacci series:'))
for i in range(1,n+1):
    print(Fibonacci(i))
    i+=1
s=0
for i in range(1,n+1):                     #finding sum of fibbonacci series
    s=s+Fibonacci(i)
print(f'The average of 1st {n} terms of fibbonacci series is:',s/n)

print()
print()
print('***********************Answer 8***********************')
print()
print()

#***********************Answer 8***********************

set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

seta=set1.union(set2)-set2.intersection(set1)          #part A
print(seta)

setB1=set1.difference(set2.union(set3))                #part B
setB2=set2.difference(set1.union(set3))
setB3=set3.difference(set2.union(set1))

setb=setB1.union(setB2).union(setB3)
print('\n',setb)

setc1=set1.intersection(set2)                           #part C
setc2=set2.intersection(set3)
setc3=set1.intersection(set3)

setc=setc1.union(setc2).union(setc3)
print('\n',setc)

set_All={1,2,3,4,5,6,7,8,9,10}                         #part D
setd=set_All.difference(set1)
print('\n',setd)

setu=set1.union(set2).union(set3)                      #part E
sete=set_All.difference(setu)
print('\n',sete)

print()
print()
print('THE END OF ASSGINMENT 3')

#*********THE END************
# Submitted by: Sparsh Aggarwal
# SID: 21104048
# branch:EE




