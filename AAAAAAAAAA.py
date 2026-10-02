def f(s1,s2,c):
    if s1+s2>=154:
        return c%2==0
    elif c==0 and s1+s2<154:
        return 0
    else:
        x=[f(s1+4,s2,c-1),f(s1*3,s2,c-1),f(s1,s2+4,c-1),f(s1,s2*3,c-1)]
        if c%2==1:
            return any(x)
        elif c%2==0:
            return any(x)
for i in range(1,143):
    if f(11,i,2)==1:
        print(i)
        break