#1
from random import randint
from re import X

from numpy import maximum


hungry= True
if hungry:
    print('Feed Me!')

#2
my_iterable =[1,2,3,4]
for item in my_iterable :
    print('You')

#3
mylist=[1,2,3,4,5,6,7,8,9,10]
for number in mylist :
    if number%2==0:
        print(number)

#4

for number01 in mylist:
    if number01%2==0:
       print(number01)
    else:
        print(f'odd number:{number01}')


#5

mystring='Hello my dear friend'
for letter in mystring:
    print(letter)

#6

d={'k1':1, 'k2':200, 'k3':300}
for love,crush in d.items(): 
    print(love)
    print(crush)

#7

mystring02='sammy'
for letter02 in mystring02:
    if letter02=='a': break
    print(letter02)

#8

mystring03='Yashvant'
for letter04 in mystring03:
    if letter04=='a':continue
    print(letter04)
    
#9 

x=0
while x<1000:
    if x==20:
        break
    print(x)
    x+=1

#10

for num in range(1,100):
    print(num)

#11

for num01 in range(1,100,2):
    print(num01)

#12

print(list(range(1,100,5))) 

#13

word01='Yashvant'
for you in enumerate(word01):
    print(you)

#14

mynum=randint(1,100)
print(mynum)

#15

mystring04='My Name is Yashvant Mahadev Hange'
mylist01=[word02 for word02 in mystring04]
print(mylist01)

#16

mylist03=[w for w in range(1,10)]
print(mylist03)

#17
mylist04=[w0*2 for w0 in range(1,100)]
print(mylist04)

#18
celcius=[0,10,20,34.5]
fahrenheit=[((9/5)*temp+32)for temp in celcius]
print(fahrenheit)

#19
mylist05=[x*y for  x in [10,20] for y in [100,200]]
print(mylist05)

#20

def check_my_list(numlist):
    for number in numlist:
        if number%2==0:
            return True
        else:
            pass

print(check_my_list([1,2,3,4,5,6,7,8,9,10]))   

#21

def check_my_list_2(number_list):
    even_numbers=[]
    for numbers in number_list:
        if numbers%2==0:
           even_numbers.append(numbers)
        else:
            pass
    return even_numbers
 
print(check_my_list_2([1,2,3,4,5,6,7,8,9,10]))

#22
work_hour=[('Uddhav',700),('Rohit',2000),('O',300)]
def student_check(work_hour):
    current_max=0
    best_student_of_month=''
    for student,hours in work_hour:
        if hours+current_max>current_max:
            current_max=hours
            best_student_of_month=student
        else:
            pass
    return(student,hours)
print(student_check(work_hour))




#23


a=int(input("Enter Your Name"))

if a>=18:
    print("Great Your to good")
else:
    print("Try again")


#24

chart=[('yash',200),('sanika',500),('samyak',400)]

def study(chart):
    initial_hours=0
    study_hours=()
    for students01,hours in chart :
        if hours>initial_hours:
           return hours==study_hours
        else:
            pass
    return(students01,hours)
print(study(chart))

#25

a=int(input("Enter seats,Declered by ECI "))
if a<=150:
    print('BJP is loosing election')
elif a>=151 and a<=340:
    print('BJP is winning')
elif a>=341 and a<=420:
    print('BJP is forming Goverment')
else:
    print('Abee Bhosdike Code hu insaan nahi!!')

#26




