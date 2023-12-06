dict1={}
print(dict1)

dict2={
    'name':'suparna',
    'sub': ['math','dsa','digital'],
    6:'age'

}
print(dict2)
#acessing values of dict using key
print(dict2['name'])

#getting all keys,values
print(dict2.keys())
print(dict2.values())


# each items (1,'green'),(2.'blue') as a pair in dic, to acess the pair 1st convert them into list , then dict 
list1=[(1,'green'),(2,'blue')]
dict4=dict(list1)
print(dict4)



# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

#display wage
age=int(input("enter your age:"))
gender=(input("enter your GENDER:"))
days=int(input("enter your age:"))
if((age>=18 )and (age <30)):
    if(gender=='F' or 'f'):
        wage=int(7500000)
        print(wage*days)
    else:
        wage=int(700)
        print(wage*days)
if((age>=30 )and (age <=40)):
    if(gender=='F' or 'f'):
        wage=int(850000000)
        print(wage*days)
    else:
        wage=int(750)
        print(wage*days)
if((age>40 )and (age <10)):
    print("sorry, not applicable")
    