# Пример 1
def task_1(n):
    X=0
    i=1
    while i<=n:
        X+=1/i
        i+=1
    return X


# Пример 2
def task_2(x, n):
    Y = x
    i = 3
    while i <= n:
        Y += x / i
        i += 2
    return Y


# Пример 3
def task_3(n):
    Y=1
    i=1
    while i<=n:
        Y*=i
        i+=1
    return Y


# Пример 4
def task_4(x, n):
    z=1
    i=2
    while i<=n:
        z*=(x+i)/i
        i+=1
    return z


# Пример 5
def task_5(x, n):
    y=1
    i=1
    while i*2<=n:
        y+=(x*i)/(2*i)
        i+=1
    return y


# Пример 6
def task_6(n):
    z=1
    i=2
    while i<=n:
        z*=i
        i+=2
    return z
