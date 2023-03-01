# 插入排序的原理是默认前面的元素都是已经排序好的，然后从后面逐个读取插入到前面
# 排序好的合适的位置，就相当于打扑克的时候每获取一张牌的时候就插入到合适的位置
# 一样。插入排序可以分为两种，一种是直接插入还一种是二分法插入，直接插入的原理
# 比较简单，就是往前逐个查找直到找到合适的位置然后插入，二分法插入是先折半查
# 找，找到合适的位置然后再插入。说到二分法查找，等排序完之后就会介绍查找，有多
# 种包括斐波那契查找，哈希查找，二分法查找等多个，其实这里面也可以使用，我们先
# 看一下简单的直接插入排序代码
# 直接插入排序
def insert_sort(array):
    if len(array) < 2:
        return array
    for i in range(1, len(array)):
        temp = array[i]
        j = i
        while j > 0:  # 步长为-1
            if array[j - 1] > temp:
                array[j] = array[j - 1]  # 如果前面比它大，就要把前面的往后挪
            else:
                break  # 前面不比它大，停止往后挪，把腾出来的位置放temp
            j -= 1
        array[j] = temp  # 把temp放进腾出来的位置里面
    return array


# 递归实现插入排序
# n表示array的长度减1
def insert_sort_1(array, n):
    if n < 2:  # 这个递归程序实在返回的时候才开始运行，看上去n在减小实际上返回的时候n在增大
        return array
    insert_sort_1(array, n - 1)  # 相当于已经把前n-1个排序好了
    temp = array[n - 1]  # 如果输入的n是len（array）的话，这个位置会有数组访问溢出
    j = n - 1
    while j > 0:
        if array[j - 1] > temp:
            array[j] = array[j - 1]  # 还是往右挪
        else:
            break
        j -= 1
    array[j] = temp
    return array


buf = [7, 6, 2, 1, 4, 3, 9]
print(insert_sort(buf))

buf1 = [6, 5, 4, 3, 2, 1]
print(insert_sort_1(buf1, len(buf1)))
