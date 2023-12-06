# #formatting 
# (n1,n2,n3)=(33,555,7777)
# print('number1={0}'.format(n1,n2),'number2={1}'.format(n1,n2))   #here 0 is the index for accesing n1, 1 index e jmn 555 a6e----------format function e sob parameter likhte ho66e

# #only accept single lenght input
# usrInput = ''
 
# while True:
#     usrInput = input("Enter a single character as input: ")
#     if len(usrInput) == 1:
#         print('Your single character input was:',usrInput)
#         break
#     print("Please enter a single character to continue\n")

# #acpect two number and print their sum using format
# a=int(input("enter 1st no:"))
# b=int(input("enter 2nd no:"))
# c=a+b
# print("sum: {0}".format(c))


# #write a python program which convert input number from other systems into decimal number system   
# number=(input("enter the number:")) #eta int typecast korbo na
# base=int(input("enter the base, you want to convert into:") )  
# temp = int(number, base) 
# print(temp) 

# #write a python program which only accepts a single character from keyboard with input string
# (a,b)=(2,4)
# print(a,b,sep=" ")
# print(a,b,sep="_")
# print(a,b,sep="$")

# #acept 3 integer in same line and display sum



# # Python program to add three numbers

# # take inputs(parini)

# num1,num2,num3 = (input("Enter three values: ")).split() 

# # add three numbers
# sum = (num1 + num2 + num3)

# # displaying the addition result
# print('{0} + {1} + {2} = {3}'.format(num1, num2, num3, sum))

# #using eval--evaluate the string into python expression
# (a,b)=(5,10)
# result=eval("a+b-4")
# print(result)

# #write a python program to check whether the given number is positive or negative
# num = float(input("Enter a number: "))
# if num >= 0:
#    if num == 0:
#        print("Zero")
#    else:
#        print("Positive number")
# else:
#    print("Negative number")



#leap year or not

def check_leap(year): 
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 

year = int(input("Enter a year: ")) 

print(f"{year} is leap year" if check_leap(year) else f"{year} is not leap year")

# Python program to find the largest number among the three input numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)


#the given value betwwen 0 to 10
number=int(input("enter a number"))
if (number >= 0) and (number <= 10):
        print("is in given range")
else:
    print("is not in the give range")
