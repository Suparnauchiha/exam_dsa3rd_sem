#The print() function in Python is often used to display output on the screen. It can also be used to print an empty line. The simplest way to do this is to call the print() function without arguments.



# python code to print numbers that
# are divisible by 3 and 5 

lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
list1=[]
for i in range(lower, upper+1):
   if((i%3==0) & (i%5==0)):
      
      list1.append(i)
print(list1,end=" ")



##find the no. from list1 which is divided by 2 and store it in list2 
list2=[]
list1=[11,22,24,36,18,23,29]

for i in list1:
            if i % 2 == 0:
                list2.append(i)
print(list2)     

# Create an empty dictionary 'd' to store the squares of numbers.
d = dict()

# Iterate through numbers from 1 to 15 (inclusive).
for i in range(1, 16):
    # Calculate the square of each number and store it in the dictionary 'd' with the number as the key.
    d[i] = i** 2

# Print the dictionary 'd' containing the squares of numbers from 1 to 15.
print(d)


#print 25 * in one line
for i in range(1,26):
    print("*", end=" ")

# Python Program to Print Square Star Pattern
 
side = int(input("Please Enter any Side of a Square  : "))

print("Square Star Pattern") 

for i in range(side):
    for i in range(side):
        print('*', end = '  ')
    print()


n = int(input('Enter number of rows : '))

i = 1
while i <= n :
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i += 1



n = int(input('Enter number of rows : '))
 
i = 1
while i <= n :
    j = n
    while j >= i:
        print("*", end = " ")
        j -= 1
    print()
    i += 1

#make a list & print the no. 1 to 100 which is divisible by 3
ls=[]
ls=[i for i in range(1,101) if i%3==0]
print(ls)

# Create an empty dictionary 'd' to store the squares of numbers.
d=dict()
d={i: i*i for i in range(1,11)}
print(d)

#whose age is not divisible by 2 and less than 40
person={'jack':38,'michale':48,'riya':57,'jordan':33}
d={k:v for (k,v) in person.items() if v%2!=0 if v<40}
print(d)

#palindrom or not
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#lcm=lasagu
# Define a function 'lcm' that calculates the least common multiple (LCM) of two numbers, 'x' and 'y'.
def lcm(x, y):
    # Compare 'x' and 'y' to determine the larger number and store it in 'z'.
    if x > y:
        z = x
    else:
        z = y
    
    # Use a 'while' loop to find the LCM.
    while True:
        # Check if 'z' is divisible by both 'x' and 'y' with no remainder.
        if (z % x == 0) and (z % y == 0):
            # If both conditions are met, 'z' is the LCM, so store it in 'lcm' and break the loop.
            lcm = z
            break
        # If the conditions are not met, increment 'z' and continue checking.
        z += 1
    
    # Return the calculated LCM.
    return lcm

# Calculate and print the LCM of 4 and 6.
print(lcm(4, 6))
# Calculate and print the LCM of 15 and 17.
print(lcm(15, 17))








# defining a function to calculate HCF  
def calculate_hcf(x, y):  
    # selecting the smaller number  
    if x > y:  
        smaller = y  
    else:  
        smaller = x  
    for i in range(1,smaller + 1):  
        if((x % i == 0) and (y % i == 0)):  
            hcf = i  
    return hcf  
  
# taking input from users  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
# printing the result for the users  
print("The H.C.F. of", num1,"and", num2,"is", calculate_hcf(num1, num2))  


#sum of given digit
n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)