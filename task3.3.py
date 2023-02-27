def task_1(lst):
    m = 0
    slst = set(lst)
    for i in slst:
        if m < max(m, lst.count(i)):
            m = lst.count(i)
            ans1 = i
    return ans1

def task_2(x, y):
    for i in range(len(x)-1):
        for q in range(i+1, len(x)):
            if (x[i] == [q]) or (y[i] == y[q]) or (abs(x[i]-x[q]) == abs(y[i]-y[q])):
                return 'YES'
    return "NO"

def task_3(x, y, xc, yc, r):
    if (x-xc)**2 + (y-yc)**2 <= r**2:
        return True
    return False

def task_4(x):
    count = 0
    for i in range(1, len(x)-1):
        if x[i-1] < x[i] > x[i+1]: count +=1
    return count

def task_5(key):
    text = open('file.txt').readlines()
    ans5 = []
    abc = ' abcdefghijklmnopqrstuvwxyz'
    for i in range(len(text)):
        str = ''
        for q in range(len(text[i])):
            for a in range(len(abc)):
                if abc[a] == text[i][q].lower():
                    str +=abc[a + key]
        ans5.append(str)
    return ans5