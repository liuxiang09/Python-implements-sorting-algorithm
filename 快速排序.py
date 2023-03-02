# https://blog.csdn.net/weixin_42437295/article/details/90771962
# 可以参考csdn里面的动画进行理解

def quick_sort(array, start, end):  # start表示数据的地址第一位，end表示数据的地址最后一位
    if start >= end:
        return array

    i = start  # 交换的位置从键值的右边一位开始，后续会先将i加一再交换
    key = array[start]  # 选定一个键值
    for j in range(start + 1, end + 1):
        if array[j] < key:
            i += 1  # i往右移动一格，这样可以保证i的位置是最后一次进行过交换的位置，也就是说i位置的数据一定比key小
            array[i], array[j] = array[j], array[i]  # 把小于key的数据放在左边，这样比key大的数据自然就到了右边
    # 循环完成后，需要把键值放在最后的i所在的位置
    # 而原来在i位置的数据一定是要比key小的（前面说过了）
    array[start] = array[i]
    array[i] = key

    quick_sort(array, start, i - 1)
    quick_sort(array, i + 1, end)
    return array


buf = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print(quick_sort(buf, 0, len(buf) - 1))
