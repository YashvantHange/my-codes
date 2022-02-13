#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3

mylist=[x for x in range(1,50) if x%2==0]
print(mylist)


#Go through the string below and if the length of a word is even print "even!
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split() :
    if len(word)%2==0 :
        print(word+ '  < this word has an even letters')

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"

# Will continue tommorow
