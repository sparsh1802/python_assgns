# Made by: Sparsh Aggarwal
# SID: 21104048
# Branch: EE

#******************************* Answer 1 ***************************************
print('Answer 1')
print()
print()

def TowerofHanoi(n , from_rod, to_rod, between_rod):
    if n == 0:            
        return None


    TowerofHanoi(n-1, from_rod, between_rod, to_rod)   


    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)


    TowerofHanoi(n-1, between_rod, to_rod, from_rod)   

n = 3                            
TowerofHanoi(n, 'A', 'C', 'B')   # A is 1st rod, B is 2nd rod and C is 3rd rod

print()
print('*'*80)
print()
#******************************* Answer 2 ***************************************
print('Answer 2')
print()
print()

def pascals_triangle(n):
    """ Defining a function to return an array containing
        the first n rows of PASCAL's TRIANGLE. """

    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascals_triangle(n - 1)
        last_row = result[-1]

        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])

        new_row += [1]
        result.append(new_row)
        return result

no_of_rows = int(input("Enter the number of rows you want:"))

if no_of_rows < 0:
    print("Number of rows cannot be -ve.")
    exit()

arr = pascals_triangle(no_of_rows)
width = len(str(arr[-1])) - 2

for i in arr:
    strng = ""

    for j in i:
        strng += (f"{j}" + "   ")

    print(strng.center(width * 2, " "))

# Iterative Procedure.

no_of_rows = int(input("Enter the number of rows you want:"))

if no_of_rows < 0:
    print("Error!: Number of rows cannot be -ve.")
    exit()

arr = [[1]]

while len(arr) < no_of_rows:

    new_row = [1]
    last_row = arr[-1]

    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])

    new_row += [1]
    arr.append(new_row)

width = len(str(arr[-1])) - 2
for i in arr:
    strng = ""

    for j in i:
        strng += (f"{j}" + "   ")

    print(strng.center(width * 2, " "))

print()
print('*'*80)
print()
#******************************* Answer 3 ***************************************
print('Answer 3')
print()
print()

int1 = int(input("Enter the first integer:"))
int2 = int(input("Enter the second integer:"))

result=divmod(int1, int2)

print(f"The Quotient is {result[0]}.\nThe remainder is {result[1]}.")

print('\nPart A\n')                                         #Part A

if callable(divmod):
    print("It's callable")
else:
    print("It's not callable")

print('\nPart B\n')                                         #Part B

value= [int1, int2] + list(result)
if all(value):
    print("All the values are not non-zero.")

else:
    print("All the values are non-zero.")

print('\nPart C\n')                                         #Part C

result_list = list(result)

for i in (4, 5, 6):
    result_list.append(i) 

new_result_list=[]
for j in result_list:
    if j>4:
        new_result_list.append(j)
print('Values greater than 4 are', new_result_list)

print('\nPart D\n')                                         #Part D

converted_set = set(new_result_list)
print(f"Converted Set : {converted_set}")

print('\nPart E\n')                                         #Part E

print("Immutable Set :", frozenset(converted_set))

print("\nPart F\n")                                         #Part F

print("Maximum value of the following numbers is", max(converted_set))

print("Hash value of max value is", hash(max(converted_set)))

print()
print('*'*80)
print()
#******************************* Answer 4 ***************************************
print('Answer 4')
print()
print()

class Students:

    def __init__(self, name:str, rollno:int):
        self.name=name
        self.rollno=rollno

    def __del__(self):
        print('Object Destroyed')


name=input('Enter the name:')
rollno=int(input('Enter the roll number:'))

stu=Students(name,rollno)      

print(f"Student name is: {stu.name} and roll number is {stu.rollno}")

print()
print('*'*80)
print()
#******************************* Answer 5 ***************************************
print('Answer 5')
print()
print()

class Employees:

    def __init__(self, name: str, salary:int ):
        self.name=name
        self.salary=salary

    def __del__(self):                   
        print('Object destroyed')

Mehak = Employees("Mehak", 40000)
Ashok = Employees("Ashok", 5000)
Viren = Employees("Ashok", 60000)

print(f"Employee name is {Mehak.name} and salary is {Mehak.salary}")
print(f"Employee name is {Ashok.name} and salary is {Ashok.salary}")
print(f"Employee name is {Viren.name} and salary is {Viren.salary}")

print('\nPart A\n')                                 #Part A

Mehak.salary=7000
print(f"Employee name is {Mehak.name} and salary is {Mehak.salary}")

print('\nPart B\n')                                #Part B

del Viren                                          #Now if i will write print(Viren), 
print()                                            # it will show an error

print()
print('*'*80)
print()
#******************************* Answer 6 ***************************************
print('Answer 6')
print()
print()

#taking input from user
George_word = input("Enter the word entered by George:").lower().strip()  

Barbie_word = input("Enter the word entered by Barbie:").lower().strip()

George_list = list(George_word)
Barbie_list = list(Barbie_word)

George_list.sort()
Barbie_list.sort()

if len(George_word)!=len(Barbie_list):          #if both words are same
    print('Letters of both word are not same.\n their friendship is fake.')

elif George_word==0:          #if user gives empty input
    print('No input from user.')

elif Barbie_list==George_list:                  #true friendship case
    print('Result: Their friendship is true.')

else:                                      
    print('Result: Their friendship is fake')


print()
print()
print('*'*30,'End of assignment-4.','*'*30)




