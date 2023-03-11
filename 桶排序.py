# 桶排序其实就是把一大串数据分别放到各个小的数组里面，然后对小的数组排序再拼接
def bucket_sort(array, bucketSize):  # 需要初始指定一个桶的大小
    length = len(array)
    # 先找到这个数组的最大值和最小值
    m_ax = array[0]
    m_in = array[0]
    for i in range(length):
        if array[i] < m_in:
            m_in = array[i]
        elif array[i] > m_ax:
            m_ax = array[i]
        else:
            continue
    # 通过最大值和最小值的差值得到所需桶的数目
    bucketCount = (m_ax - m_in) // bucketSize + 1
    buckets = [[] for i in range(bucketCount)]  # 直接构建二维列表
    # 把所有数据放进它所属于的桶内
    for i in range(length):
        buckets[(array[i] - m_in) // bucketSize].append(array[i])
    #  桶内排序，使用快速排序算法
    for i in range(bucketCount):
        quick_sort(buckets[i], 0, len(buckets[i]) - 1)
    res = []
    for i in range(len(buckets)):  # 分别将各个桶内的数提出来，压入结果
        for j in range(len(buckets[i])):
            res.append(buckets[i][j])
    return res


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


numlist = [2, 6, 9, 3, 5, 1, -9, 7, -3, -1, -6, 8, 0]
print(bucket_sort(numlist, 5))
