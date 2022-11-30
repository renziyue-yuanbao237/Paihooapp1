def _roll(num):
    def f(n,x):
        li=[]
        a=[0,1,2,3,4,5,6,7,8,9,'A','b','C','D','E','F']
        b=[]
        while True:
            s=n//x
            y=n%x
            b=b+[y]
            if s==0:
                break
            n=s
        b.reverse()
        for i in b:
            li.append(str(a[i]))
        li="".join(li)
        return int(li)
    di=["星期日","星期一","星期二","星期三","星期四","星期五","星期六"]
    num=int(str(f(num,7))[::-1][0])
    return di[num]
def roll(startwith,n):
    for x in range(startwith,n+startwith):
        yield _roll(x)

