import re
x = input('Enter Something...')
y = re.findall(r'[\d\?{0-3}\d$]+',x)
def f(y):
    if len(y) == 1:
        qnum = 0
        dig = 0
        count_10 = False
        for i in y:
            pass
        for ch in i:
            if ch.isdigit():             
                if int(ch) + dig == 10:
                    if qnum != 3:
                        return 'false'
                    count_10 = True
                dig = int(ch)
                qnum = 0    
            elif ch == '?':
                qnum += 1
        return 'true' if count_10 else 'false'
    else:
        for i in y:
            if i == '6???4' and i == '4???6' and i == '1???9' and i == '5???5' and i == '9???1' and i == '8???2' and i =='2???8' and i == '3???7' and i == '7???3':
                l = True
            if y[len(y)-1] == '1???9' and y[len(y)-1] == '9???1' and y[len(y)-1] == '5???5' and y[len(y)-1] == '8???2' and y[len(y)-1] =='2???8'and y[len(y)-1] == '6???4' and y[len(y)-1] == '4???6'and y[len(y)-1]  == '3???7' and y[len(y)-1] == '7???3':
                l = True      
            else:
                l = False
        return l


print(f(y))


########################################################
Method:2
x = input('Enter any String:');chunck_size = 5;k =5;y = [];j = []
while chunck_size <= len(x)-3:
    if k == 5:
        y.append(x[0:5])
        k = k+1
    y.append(x[chunck_size-1 : chunck_size+4])
    chunck_size = chunck_size + 4
for i in range(len(y)):
    if y[i] in ['6???4','4???6','1???9','5???5','9???1','8???2','2???8','3???7','7???3']:        
        j.append(y[i])
print(True) if len(j)>=1 else print(False)

