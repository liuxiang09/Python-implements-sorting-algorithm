# 选择排序和冒泡排序有一点点像，选择排序是默认前面都是已经排序好的，然后从后面
# 选择最小的放在前面排序好的的后面，首先第一轮循环的时候默认的排序好的为空，然
# 后从后面选择最小的放到数组的第一个位置，第二轮循环的时候默认第一个元素是已经
# 排序好的，然后从剩下的找出最小的放到数组的第二个位置，第三轮循环的时候默认前
# 两个都是已经排序好的，然后再从剩下的选择一个最小的放到数组的第三个位置，以此
# 类推。

def select_sort(array):
    for i in range(0, len(array)):
        index = i
        for j in range(i+1, len(array)):
            if array[j] < array[index]: # 把最小的选择出来，放到第一位
                index = j
        if index != i:
            array[i], array[index] = array[index], array[i]  # swap
    return array


# 选择排序的递归实现
# n的初值赋为0,n的作用相当于双层循环中的i
def select_sort_1(array, n):
    if n == len(array):
        return array
    if len(array) == 0:
        return array

    global j
    index = n
    for j in range(n, len(array)):
        if array[j] < array[index]:
            index = j
    if n != index:
        array[n], array[index] = array[index], array[n]

    select_sort_1(array, n+1)
    return array


buf = [3, 5, 6, 1, 0, -1]
print(select_sort_1(buf, 0))
