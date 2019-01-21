# To check wether a given list is in fibbonaci series or not
l = [1,2,3,5,8,13,21]
def is_fibbonaci(l):
    
    n = len(l)
    if n%2 == 0:
        n = n/2 
        n = int(n)
    else:
        n = n/2
        n = int(n) + 1
    for i in range(n):
        if l[i] + l[i+1] != l[i+2]:
            break
    if i == n-1:
        print('The Given List is in fibbonacci series')

is_fibbonaci(l)
