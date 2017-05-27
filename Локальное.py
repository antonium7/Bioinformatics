# локальное выравниивание
t = 'ccttggttccttgg'.upper() #2
m = len(t)

s = 'cctgg'.upper() #1
n = len(s)
        
p = []

for i in range(m+1): # создаем 2-хмерную матрицу
    column = []
    for j in range(n+1):
        column.append(0)
    p.append(column)
    

for i in range(n):
    for j in range(m):
        left = p[j+1][i]-2
        up = p[j][i+1]-2
        if s[i]==t[j]:
            diag = p[j][i] + 1
        else:
            diag = p[j][i] - 1
        p[j+1][i+1]=max(left,up,diag, 0)
# заполнение матрицы штрафов и премий


Numbers = []
for i in range(n+1):
    for j in range(m+1):
        Numbers.append(int(p[j][i]))
max_number = max(Numbers)
# поиск максимального значения в матрице

StartIndex = []
for i in range(n+1):
    for j in range(m+1):
        if p[j][i] == max_number:
            x,y = j,i
            StartIndex.append([x,y])

            
result1LIST = []
result2LIST = []



'''
хочу сделать с пробелами

for indexes in StartIndex:
    result1 = ''
    result2 = ''
    j = int(indexes[0])
    i = int(indexes[1])
    while p[j][i]:
        if int(p[j][i]) != 0:
            result1 = s[i-1] + result1
            result2 = t[j-1] + result2
            j-=1
            i-=1
        elif int(p[j][i]) == 0:
            if int(p[j][i+1]) != 0:
                result1 = '_' + result1
                result2 = t[j-1] + result2
                j-=1
                i+=i
            elif int(p[j+1][i]) != 0:
                result1 = s[i-1] + result1
                result2 = '_' + result2
                i-=1
                j+=j
            elif int(p[j+1][i]) == 0 and int(p[j][i+1]) == 0:
                break
    result1LIST.append(result1)
    result2LIST.append(result2)

for i in p:
    print(i)
print(max_number)
print(StartIndex)
print(result1LIST)
print(result2LIST)
        

result1LIST = []
result2LIST = []
result1 = ''
result2 = ''

'''
for indexes in StartIndex:
    result1 = ''
    result2 = ''
    j = int(indexes[0])
    i = int(indexes[1])
    while p[j][i]:
        if int(p[j][i]) != 0:
            result1 = s[i-1] + result1
            result2 = t[j-1] + result2
            j-=1
            i-=1
        else:
            break
    result1LIST.append(result1)
    result2LIST.append(result2)

for i in p:
    print(i)
print(max_number)
print(StartIndex)
print(result1LIST)
print(result2LIST)
        

result1LIST = []
result2LIST = []
result1 = ''
result2 = ''

'''
Index_of_max_numbers = []
for i in range(n+1):
    for j in range(m+1):
        if int(p[j][i])==int(max_number):
            result1=t[j-1] + result1
            result2=s[i-1] + result2
            q = i
            w = j
            Index_of_max_numbers.append(str(q)+':'+ str(w))
            while q and w:
                if int(p[w-1][q-1])!= 0:
                    result1=t[w-2]+result1
                    result2=s[q-2]+result2
                elif int(p[w-1][q-1])== 0:
                    break
                result1LIST.append(result1)
                result2LIST.append(result2)
                q-=1
                w-=1
        result1 = ''
        result2 = ''
print(Index_of_max_numbers)
print(result1LIST)
print(result2LIST)
        '''
