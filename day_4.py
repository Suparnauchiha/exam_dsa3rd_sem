#empty tuple
t1=()
print(t1)

#convert list to tuple
l1=[20,88,6,3]
t2=tuple(l1)
print(t2)

#acessing tuple element
print(t2[0])

print(max(t2))
print(min(t2))

#tuple ke list e convert kore append ,remove kora jay

#using asteric 
c=('a','b','c','d','e')
(g,h,*i)=c
print(g)
print(h)
print(*i)