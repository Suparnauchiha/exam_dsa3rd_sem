print(-10//3) #it will not print 3..instead will print -4
#find out the img,real,conjugate part
import cmath
 
# Initializing real numbers
x = 5
y = 3
 
# converting x and y into complex number
z = complex(x,y)
print(z)
 
# printing real and imaginary part of complex number
print ("The real part of complex number is : ",end="")
print (z.real)
 
print ("The imaginary part of complex number is : ",end="")
print (z.imag)

#find out perimeter of circle
r=float(input("enter the radius:"))
area=3.14*r*r
circum=2*3.14*r
print("the area of the circle",area)
print("the circumference of the circle ",circum)

#converting ferhenheight to centigrate
f=float(input("enter a ferhenheight temperature:"))
c=(5*(f-32))/9
print(c)


