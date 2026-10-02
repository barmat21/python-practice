a=0
for i1 in range(7):
    for i2 in range(7):
        for i3 in range(7):
            for i4 in range(7):
                if i1>i2>i3>i4:
                    a+=1
print(a)

with open('1.txt',encoding='utf=8') as o:
    o=o.read().strip().split('\n')
    z=[]
    for i in o:
        a=i.split('\t')
        a=list(map(int,a))
        z.append(a)
    a=0
    for i in z:
        if len(i)==len(set(i)):
            if 2*(max(i)+min(i))<=sum(i)-max(i)-min(i):
                a+=1
print(a)



c={}
def f(n):
    if n < 2:
        return 5
    elif n in c:
        return c[n]
    else:
        c[n]=5*f(n-1)-4*f(n-2)
        return c[n]
print(f(13))


with open('17 (1).txt',encoding='utf-8') as o:
    o=o.read().strip().split()
    x=[]
    for i in o:
        if i[-2:]=='17':
            x.append(int(i))
    max_x=max(x)
    o=list(map(int,o))
z=[]
v=[]
a=0
n=0
for i in range(len(o)-2):
    z.append([o[i],o[i+1],o[i+2]])
for i in range(len(z)):
    for j in range(len(z[i])-2):
        if z[i][j]%5==0 or z[i][j+1]%5==0 or z[i][j+2]%5==0:
            if (len(str(abs(z[i][j]))) == 4) + (len(str(abs(z[i][j + 1]))) == 4) + (len(str(abs(z[i][j + 2]))) == 4) == 2:
                if sum(z[i])>max_x:
                    v.append(sum(z[i]))
                    a+=1
print(a)
print(max(v))


def f(k1,h):
    if k1>=92:
        return h%2==0
    if h==0:
        return False
    else:
        z = [i for i in range(1, k1 + 1) if k1 % i == 0]
        x=[]
        for j in z:
            x.append(f(k1+j,h-1))
        if h==3 or h==1:
            return any(x)
        else:
            return all(x)
for i in range(1,92):
    if f(i,3)==True and f(i,1)==False:
        print(i)



with open('33.txt',encoding='utf-8') as o:
    z=[]
    for i in o.readlines():
        z.append(list(map(int,i.split())))
    n=0
    sum_nep=0
    sum_pov=0
    for i in z:
        c={}
        for j in i:
            if j in c:
                c[j]+=1
            else:
                c[j]=1
        x=[]
        for k,v in c.items():
            x.append(v)
        if x.count(2)==2 and x.count(1)==2:
            for k,v in c.items():
                if v==2:
                    sum_pov+=k
                elif v==1:
                    sum_nep+=k
            if sum_pov<sum_nep:
                n+=1
            sum_nep = 0
            sum_pov = 0
print(n)

import turtle as t
m=5
t.tracer(0)
for i in range(11):
    t.forward(36*m)
    t.right(72)
for x in range(-90,90):
    for y in range(-90,90):
        t.up()
        t.goto(x*m,y*m)
        t.down()
        t.dot()
t.done()
with open('17 (2).txt',encoding='utf=8') as z:
    z=z.read().split()
    z=list(map(int,z))
a=0
v=[]
for i in range(len(z)-1):
    v.append(z[i:i+2])
for i in range (len(v)):
    for j in range(2):
        if v[i][j]%3==0:
            a+=1
    v[i].append(a)
    a=0
z=[]
b=0
for i in v:
    if i[-1]==1 or i[-1]==2:
        z.append(i[0]+i[1])
        b+=1
print(b)
print(max(z))



import turtle as t
m=10
t.tracer(0)
for i in range(2):
    t.forward(3*m)
    t.left(90)
    t.backward(10*m)
    t.left(90)
t.up()
t.backward(10*m)
t.right(90)
t.forward(8*m)
t.left(90)
t.down()
for i in range(2):
    t.forward(16*m)
    t.right(90)
    t.forward(8*m)
    t.right(90)
t.up()
for x in range(-30,30):
    for y in range(-30,30):
        t.up()
        t.goto(x*m,y*m)
        t.dot()


