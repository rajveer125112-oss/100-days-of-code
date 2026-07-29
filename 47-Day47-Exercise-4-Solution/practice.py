
a=input("Enter the word =")

r=input("Do you want to encode it or decode it? =")

m=[]
v=[]
p=[]
w=[]
x=[]
if r=="encode":
    if len(a)>=3:
        m.append(a[1:len(a)])
        m.append(a[0])
        k=m[0]+m[1]
        h1="ghs"
        h2="aps"
        t=[]
        t.append(k)
        t.append(h1)
        t.append(h2)
        n=t[1]+t[0]+t[2]


        print(n)
    else:
        v.append(a[0])
        v.append(a[1])
        g=v[1]+v[0]
        print(g)
elif r=="decode":
    if len(a)>=3:
        p.append(a[0:3])
        p.append(a[-3:])
        p.append(a[3:len(a)-3])
        
        p.pop(0)                #First time I removed a character now list will consist of 2 items so Item which was at index 1 will be at index 0 after I popped the earlier one
        p.pop(0)
        d=p[0]
        w.append(d[0:len(d)-1])
        w.append(d[-1])
        s=w[1]+w[0]
        print(s)

    else:
        x.append(a[0])
        x.append(a[1])
        print(a[1]+a[0])
