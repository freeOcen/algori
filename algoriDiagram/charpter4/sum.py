def sum_a(arr):
    if arr ==[]:
        s=0
    else:
        s=arr[0] + sum_a(arr[1:len(arr)])
    return s

#count the array length
def count(arr):
    if arr==[]:
        return 0
    else :
        return 1+count(arr[1:len(arr)])

#find the max value in the list
def findMax(list):
    if len(list) ==2:#基线条件
        return list[0] if list[0]>list[1] else list[1]
    #递归条件
    sub_max = findMax(list[1:]) 
    return list[0] if list[0]>sub_max else sub_max

    

arr = [1,2,3,12,4]
# print(sum_a(arr))
# print(count(arr))
print(findMax(arr))
