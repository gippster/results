def task_1(lst, var):
    lst=sorted(lst)
    middle=len(lst)//2
    answer=None
    if var==lst[middle]:
        answer=middle
    else:
        while answer==None:
            if var<lst[middle]:
                lst=lst[:middle-1]
                middle = len(lst) // 2
                if var == lst[middle]: answer = middle
            elif var>lst[middle]:
                lst = lst[middle:]
                middle = len(lst) // 2
                if var == lst[middle]: answer = middle
    return str(answer)
def task_2(chislo):
    prostoe=True
    for i in range(2,chislo):
        if chislo%i==0:
            prostoe=False
    return prostoe