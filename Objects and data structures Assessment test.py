# Number Question

a=4*(6+5)
print(input(a))

#Strings
s='Hello'
print(s[1])
s[::-1]
print(s)

#LIST

list[0,0,0]
print(list)

list=[0]
print(list*3)

list3=[1,2,[3,4,'Hello']]
list3[2][2]='goodbye'
print(list3)

list4= [5,3,4,6,1]
list4.sort()
print(list4)

#Dictionaries

d={'simple_key':'Hello'}
print(d.get('simple_key'))

d2 = {'ka':{'k2':'hello'}}
print(d2['ka']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])


#Sets
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))