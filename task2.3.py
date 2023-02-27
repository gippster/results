
def task_1(str):
    str=str.split()
    return len(str[-1])


def task_2(str):
    str = str.split()
    for i in range(1,len(str),2):
       str[i],str[i-1]=str[i-1],str[i]
    return " ".join(str)


def task_3(str):
    flag=0
    str=str.lower()
    str=str.split()
    for i in range(1,len(str)):
        if str[i-1][-1]==str[i][0]: flag+=1
    return flag
