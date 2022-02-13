#my list
from multiprocessing.sharedctypes import Value
from random import randint


mylist1=[1,2,3,4,5]
for you in mylist1:
    print(you)

#little Advanced Example

mylist2=[1,2,3,4,5,6,7,8]
for num in mylist2:
    if num%2==0 :
      print(num)    

#Getting Even and ODD


mylist3=[1,2,3,4,5,6,7,8,9,10,11,12]
for num1 in mylist3:
    if num1%2==0:
        print(num1)
    else:
        print(f'This is odd number:{num1}')

#For string we use

mystring='hello'
for this in mystring:
    print(this)        

#For dircet string we use

for they in 'Hello' :
    print(they)


#for tuples: for unpacking tuples in lists

mylist4=[(1,2),(3,4),(5,6)]
for (a,b) in mylist4:
    print(a)
    print(b)

#For Dictonary
# Dictionaries are unordered, we get data only for small dictionaries but their is no gurrenty for getting values for large dictionaries

d={'k1':100,'k2':200,'k3':300}
for(keys,value) in d.items():
    print(value)


#Continue function

mystring20='MY NAME IS YASHVANT MAHADEV HANGE'
for letter20 in mystring20:
    if letter20=='A': continue
    print(letter20)

#Pass Function

mystring30='MY NAME IS IRON MAN'
for letter5 in mystring30:
    if letter5=='E':
        break
    print(letter5)

##break example for integers

X=0
while X<10:
    if X==6:
        break
    print(X)
    X+=1

#Useful oprators in python

#1

for num10 in range(0,10):
    print(num10)

#2

for num3 in range(0,10,2):
    print(num3)

#3
print(list(range(0,11,1)))

#4

index_count=0
for letter10 in 'IRON MAN':
    print('At index {} the letter10 is {}'. format(index_count,letter10))
    index_count+=1


#for getting random number

mynum=randint(0,10000)
print(mynum)

#List Comprehensions in Python

#List comprehensions are a unique way of queckly creating a list with python

stringyou='MY NAME IS YASHVANT HANGE'
mylist5=[letter1 for letter1 in stringyou]
print(mylist5)

