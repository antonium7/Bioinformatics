alphabet = ('A', 'C', 'G', 'T')

s1 = input("S1").upper()
        
s2 = input("S2").upper()

x = len(s2)
y = len(s1)

p = []

for i in range (y+1):
    col = []
    for j in range (x+1):
        col.append(0)
    p.append (col)

for i in  range(y):
    for j in range(x):
        left = -2 + p[i+1][j]
        up = -2 + p[i][j+1]
        if s1[i] == s2[j]:
            diag = p[i][j] + 1
        else:
            diag = p[i][j] - 1
        p[i+1][j+1] = max(left, up, diag)

for i in p:
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


Res1 = []
Res2 = []


for i in range(len(index_max)):
    res1 = ''
    res2 = ''
    a, b = int(index_max[i][0]), int(index_max[i][1])
    print('a:', a, 'b:', str(b))
    while  a>=0 and b>=0:
        if a==0 and b!=0:
            res1 = '_' + res1
            res2 = s2[b-1] + res2
            b-=1
        elif b==0 and a!=0:
            res1 = s1[a-1] + res1
            res2 = '_' + res2
            a-=1
        elif a==0 and b==0:
            break
        elif p[a][b]==p[a-1][b-1]+1:
            res1 = s1[a-1] + res1
            res2 = s2[b-1] + res2
            a-=1
            b-=1
        elif p[a][b]==p[a-1][b-1]-1:
            res1 = s1[a-1] + res1
            res2 = s2[b-1] + res2
            a-=1
            b-=1
        elif p[a][b]==p[a-1][b]-2:
            res1 = '_' + res1
            res2 = s2[b-1] + res2
            b-=1
        elif p[a][b]==p[a][b-1]-2:
            res1 = s1[a-1] + res1
            res2 = '_' + res2
            a-=1
    Res1.append(res1)
    Res2.append(res2)
    res1 = ''
    res2 = ''

print(Res1)
print(Res2)


'''
for i in range(len(index_max)):
    res1 = ''
    res2 = ''
    a, b = int(index_max[i][0]), int(index_max[i][1])
    print('a:', a, 'b:', str(b))
    while  a>=0 and b>=0:
        if p[a][b]==p[a-1][b-1]+1:
            res1 = s1[a-1] + res1
            res2 = s2[b-1] + res2
            a-=1
            b-=1
        elif p[a][b]==p[a-1][b-1]-1:
            res1 = s1[a-1] + res1
            res2 = s2[b-1] + res2
            a-=1
            b-=1
        elif p[a][b]==p[a-1][b]-2:
            res1 = '_' + res1
            res2 = s2[b-1] + res2
            b-=1
        elif p[a][b]==p[a][b-1]-2:
            res1 = s1[a-1] + res1
            res2 = '_' + res2
            a-=1
        if a==0 and b!=0:
            res1 = '_' + res1
            res2 = s2[b-1] + res2
            b-=1
        elif b==0 and a!=0:
            res1 = s1[a-1] + res1
            res2 = '_' + res2
            a-=1
    Res1.append(res1)
    Res2.append(res2)
    res1 = ''
    res2 = ''


    


    while p[a][b] and a>=0 and b>=0:
        if a!=0 and b!=0:
            if p[a][b]==p[a-1][b-1]+1:
                res1 = s1[a-1] + res1
                res2 = s2[b-1] + res2
                a-=1
                b-=1
            elif p[a][b]==p[a-1][b-1]-1:
                res1 = s1[a-1] + res1
                res2 = s2[b-1] + res2
                a-=1
                b-=1
            elif p[a][b]==p[a-1][b]-2:
                res1 = '_' + res1
                res2 = s2[b-1] + res2
                b-=1
            elif p[a][b]==p[a][b-1]-2:
                res1 = s1[a-1] + res1
                res2 = '_' + res2
                a-=1
        if a==0 or b==0:
            if a==0 and b!=0:
                res1 = '_' + res1
                res2 = s2[b-1] + res2
                b-=1
            elif b==0 and a!=0:
                res1 = s1[a-1] + res1
                res2 = '_' + res2
                a-=1
    Res1.append(res1)
    Res2.append(res2)
    res1 = ''
    res2 = ''

'''
