def task_1(N):
    x=1
    for i in range(1,N+1):
       x*=i
    return x


def task_2(N):
    f1 = 0
    f2 = 1
    for i in range(2, N):
        f1, f2 = f2, f2+f1

    return f2


def task_3(N):
    d=set()
    for i in range(1,N+1):
        if N%i==0:
            d.add(i)
    return sorted(d)
