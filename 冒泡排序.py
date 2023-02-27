# 冒泡排序
def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]  # swap函数
    return array


# 冒泡排序（修正）
def bubble_sort_1(array):
    length = len(array)
    flag = True
    while flag:
        flag = False  # 如果没有经历swap，flag就会保持False，则会在while处退出循环
        for j in range(0, length-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]  # swap函数
                flag = True  # 如果交换了就把flag赋值为True，否则说明已经排序好了，节省剩余时间
        length -= 1
    return array


buf = [3, 5, 6, 1, 0, -1]
print(bubble_sort(buf))
print(bubble_sort_1(buf))
