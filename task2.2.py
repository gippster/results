import math
# Пример 1
def task_1(A):
    sum=0
    for i in range(0,len(A)):
        if A[i]>0: sum+=A[i]
    return sum

# Пример 2
def task_2(A):
    med=0
    for i in range(0,len(A)):
        med+=A[i]/len(A)
    return med

# Пример 3
def task_3(A):
    sum=0
    med=0
    for i in range(0,len(A)):
        med += A[i] / len(A)
    for i in range(0,len(A)):
        sum+=(A[i]-med)**2
    return math.sqrt(sum/len(A))
