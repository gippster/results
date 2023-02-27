def task_1(str):
    str1 = set()
    dic = {}
    for i in str:
        if i in 'qwertyuiopasdfghjklzxcvbnm':
            str1.add(i)
            dic[i] = str.count(i)
    return dic

def task_2(list):

    return sum(set(list))

def task_3(cities):
    str=", ".join(cities)+'.'
    return str


def task_4(a, b):
    ans=set(a)&set(b)
    return list(ans)
