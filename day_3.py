l=list('suparna') #list e typecast kore dilam
print(l)

#list concatenation
l1=[1,44,66]
l2=[55,88,89]+l1
print(l2)
l1.append(333333)
print(l1)
#cpmparison in list leght
print(l2>l1)

#replace method in string
str="urmi"
print(str.replace('m','n'))

#comparison of string based on ascii value
s1="urmi"
s2="URMI"
print(s1>s2) #true bcz lower case er ascii value besi

#insert(index no. , value)
names=['urmi','suparna','piu']
names.insert(1,'dolly')
print(names)
#remove
names.remove("suparna")
print(names)
#index-- to acess index
i=names.index("piu")
names[i]="piudi"
print(names)

print(sorted ,names) 
#sorted bulid in function
#reverse list
names.reverse()
print(names)

size=len(names)
print("size of the list:",size)

names.clear()
print(names)
