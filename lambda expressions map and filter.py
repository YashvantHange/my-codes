from tkinter.font import names
from unicodedata import name
from numpy import square

#1
my_Number=[1,2,3,4,5,6,7,8,9,10]
for item in map(square,my_Number):
    print(item)

#2
print(list(map(lambda item:item**2,my_Number)))



#3

in_number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for number in in_number_list:
    pass
print(list(map(lambda number:number*120,in_number_list)))



#4 extra try

my_list=[1,2,3,4,5,6,7,8,9,10,11,12]
for num in my_list:
    pass
print(list(map(lambda num: num*20,my_list)))



#5

def check_evns(no):
    return no%2==0
no=[1,2,3,4,555,55,3333,562,345463,]

print(list(filter(check_evns,no)))

# Splicer

def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]

names=['Hi','Hello','Yashvant']
print(list(map(splicer,names)))       
 
#7

def letter(word):
    if word%2==0 :
        return 'EVEN'

name=['hELlo','Yashvant','samyak','sonali','God']

print(list(map(splicer,name)))