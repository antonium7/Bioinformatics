alphabet = ('G','T','A','C')

s = input('Sequence1:').upper()
n = len(s)
for i in range(n):
    while s[i] not in alphabet:
        s= input('Please try again - Sequence1:')
        
t = input('Sequence2:').upper()
m = len(t)
for i in range(m):
    while t[i] not in alphabet:
        s= input('Please try again - Sequence2:')
p = []
way = []

for i in range(m+1):
    #создание 2-хмерного массива
    column = []
    way_column = []
    for j in range(n+1):
        column.append(0)
        way_column.append('_')
    p.append(column)
    way.append(way_column)

for i in range(m+1):
    #инициализация нулевого рядка и столбика 
    p[i][0]=(-2)*i
    way[i][0]='↑'
for j in range(n+1):
    p[0][j]=(-2)*j
    way[0][j]='←'
way[0][0]='↖'

for i in range(m):
    for j in range(n):
        left = p[i+1][j]-2
        up = p[i][j+1]-2
        if s[j]==t[i]:
            diag = p[i][j] + 1
        else:
            diag = p[i][j] - 1
        p[i+1][j+1]=max(left,up,diag)
        #заполнение матрицы премий и штрафов
        if p[i+1][j+1]==left:
            way[i+1][j+1]='←'
        elif p[i+1][j+1]==up:
            way[i+1][j+1]='↑'
        else:
            way[i+1][j+1]='↖'
        #заполнение матрицы пути
            
for i in p:
    print(i)
for i in way:
    print(i)

result1 = ''
result2 = ''
#обратный путь
while n or m:
    if way[m][n]=='↖':
        result1=t[m-1]+result1
        result2=s[n-1]+result2
        n = n-1
        m = m-1
    elif way[m][n]=='←':
        result1='_'+result1
        result2=s[n-1]+result2
        n = n-1
    else:
        result1=t[m-1]+result1
        result2='_'+result2
        m = m-1
print(result2)
print(result1)
