#快速排序
def quicksort(array):
    if len(array)<2:
        return array#基线条件
    else:
        pivot = array[0]
        #递归条件
        less = [i for i in array[1:] if i<=pivot]
        great = [i for i in array[1:] if i>pivot]

        return quicksort(less) + [pivot] + quicksort(great)

arr = [21,1,32,13,5]
print(quicksort(arr))