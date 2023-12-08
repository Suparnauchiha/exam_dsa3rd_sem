# Write a program to print fibonacci series upto n terms in python
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()


# Program to check if a number is prime or not
# To take input from the user
num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)    



P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))  
   
# To Swap the values of two variables  
P, Q = Q, P  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  






age1 = int(input("Enter the Age of Ram :"))
age2 = int(input("Enter the Age of Shyam :"))
age3 = int(input("Enter the Age of Ajay :"))
if(age1<age2 and age1<age3):
	print("The Youngest Age is Ram")
elif(age2<age1 and age2<age3):
	print("The Youngest Age is Shyam")
else:
	print("The Youngest Age is Ajay")









n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)





