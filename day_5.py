#slicing method 
t1=list("abcdef")
print(t1)
print(t1[2:4]) #2 theke (4-1)=3 obdhi print hobe

# using "is" ,"in"
if "a" in t1:
    print("a is present")

else:
    print("a is not present")

#reverse the tuple.. in the same way list can be reversed
t3=(5,44,6666,2)
t3=t3[::-1]
print("reversing t3:" ,t3)    

#accessing ,modify tuple 
t4=("orange",[13,33,55,6],[55,777,4,3,9])
print(t4[2][3])
t4[1][1]=99999990
print("after modifying:", t4)

#unpacking tuples
(a,b,c,d)=t3
print(a)
print(b)
print(c)
print(d)

#to know theoccure 

t5=(4,6,7,6,7,6,7,333)
print("occurenece of 6 in t5:",t5.count(6))

(a,b)=(2,4)
print(a,b,sep="+")
print(a,b,sep="=")
print(a,b,sep="................")

print("city name:"+" kolkata") #to concatenate two print statement



print("suparna",end="     ""paul") #end is used for space or next line