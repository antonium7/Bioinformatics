alphabet = ['A', 'C', 'G', 'T']

s1 = input("S1").upper()
        
s2 = input("S2").upper()

x = len(s2)
y = len(s1)

p = []
way = []

for i in range (y+1):
    col = []
    way_col = []
    for j in range (x+1):
        col.append(0)
        way_col.append(0)
    p.append (col)
    way.append(way_col)
    
for i in range(y+1):
    way[i][0] = '↑'

for j in range(x+1):
    way[0][j]= '←'
    
way[0][0] = '-'

for i in  range(y):
    for j in range(x):
        left = -2 + p[i+1][j]
        up = -2 + p[i][j+1]
        if s1[i] == s2[j]:
            diag = p[i][j] + 1
        else:
            diag = p[i][j] - 1
        p[i+1][j+1] = max(left, up, diag)
        if max(left, up, diag) == left:
            way[i+1][j+1] = '←'
        elif max(left, up, diag) == up:
            way[i+1][j+1] = '↑'
        else:
            way[i+1][j+1] = '↖'
for i in p:
    print(i)
for i in way:
    print(i)
    

re = p[y]
g = [h[x] for h in p]
Index = re+g
print(Index)
max = max(Index)
print(max)


index_max =[]
for i in  range(y+1):
    if p[i][x] == max:
        index_max.append([i,x])
for j in range(x+1):
    if p[y][j] == max:
        index_max.append([y,j])
            
print(index_max)

res1 = ''
res2 = ''
Res1 = []
Res2 = []
for i in range(len(index_max)):
    a, b = int(index_max[i][0]), int(index_max[i][1])
    while a>=0 or b>=0:
        if way[a][b] == '↖':
            res1 = s1[a-1] + res1
            res2 = s2[b-1] + res2
            a-=1
            b-=1
        elif way[a][b] == '←':
            res1 = '_' + res1
            res2 = s2[b-1] + res2
            b-=1
        elif way[a][b] == '↑':
            res1 = s1[a-1] + res1
            res2 = '_' + res2
            a-=1
        else:
            break
    Res1.append(res1)
    Res2.append(res2)
    res1 = ''
    res2 = ''
    
print(Res1)
print(Res2)
