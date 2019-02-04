#for printing numbers from 0 to 9
l = [x for x in range(0,10)]
print(l)

#for printing squares of numbers
l = [x*x for x in range(1,5)]
print(l)

#for printing numbers which are multiples of three
l = [x*3 for x in range(1,5)]
print(l)

#for printing letters in a word
l = [x for x in 'Raghava']
print(l)

#for printing words in list
l = ["Mango","Apple","chikoo","Banana"]
x = [i[0] for i in l]
print(x)

#for converting a word to lower case
l = [i.lower() for i in 'RAGHAVA']
print(l)

#checking wether it is a digit or not
l = [x for x in "Hello 12345 World" if x.isdigit()]
print(l)

#doubling the through function
def double(x):
    return x*2
l = [double(x) for x in range(1,11)]
print(l)

#doubling a number through condition
def double(x):
   return x*2
l = [double(x) for x in range(1,11) if x%2==0]
print(l)

#printing the sum in two sequences
l = [x + y for x in range(1,10) for y in range(10,20)]
print(l)
