# 1

def lesser_of_two_evens(a,b): 
    if a%2==0 or b%2==0:
        if a<b:
            return a
        else:
            return b
    else:
        return "Code is Not working"

print(lesser_of_two_evens(2,5))

#2

#def animal_crackers(text):
#    if text == ("Levelheaded Llama").split(text):
#        return True
#   else: 
#        False_

#print(animal_crackers("L"))

#3 

def makes_twenty(n1,n2):
    if n1+n2==20:
        return True
    else:
        return  False

print(makes_twenty(10,20))
print(makes_twenty(10,10))

#4


def old_macdonald(name):
    first_letter= name[0]
    second_letters=name[1:3]
    third_letter=name[3]
    other_letter=name[4:9]
    return first_letter.upper() + second_letters+third_letter.upper()+other_letter
print(old_macdonald("macdonald"))


#5
def master_yoda(text):
    word_list=text.split()
    reversed_word_list=word_list[::-1]
    return reversed_word_list
print(master_yoda("I Am home"))

#6

def almost_there(n):
    return (abs(100-n)<=10) or (abs(200-n)<=10)

print(almost_there(90))

#7

def blackjack(a,b,c):
    sum=a+b+c
    if sum<=21:
        return sum
    elif sum>=21 :
        return sum-10
    else:
        return "Bust"
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
    

#Rest all i will solve after II become eligible
