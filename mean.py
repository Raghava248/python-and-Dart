#You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. 
#The marks can be floating values. 
#The user enters some integer N followed by the names and marks for students. You are required to save the record in a dictionary data type. 
#The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.



from statistics import mean
d = {}
n = int(input('Enter some value'))
for i in range(n):
    key = input('Key?')
    value = [int(x) for x in input('enter value').split(',')]
    d[key] = value

j = input('Enter name of student')
if j in d.keys():
    print(mean(d[j]))
