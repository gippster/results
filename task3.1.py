def task_1(str):
    str=str.split('. ')
    str[-1]=str[-1][:-1]
    ans={}
    for i in range(0,len(str)):
        ans[str[i]]=len(str[i].split())
    return ans
print(task_1('First sent. Second sent and. Third sent and other.'))
import math
def task_2(x1,y1,x2,y2):
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance
print(task_2(2,5,4,9))