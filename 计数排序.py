# 计数排序
# 计数排序思路
# 1. 找出待排序的数组中最大和最小的元素
# 2. 统计数组中每个值为i的元素出现的次数，存入数组C的第i项
# 3. 对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）
# 4. 反向填充目标数组：将每个元素i放在新数组的第C[i]项，每放一个元素就将C[i]减去1

# 计数排序的优缺点
# 优点：时间复杂度O(n+k)，空间复杂度O(n+k)，k是待排序数组中最大值和最小值的差值
# 缺点：计数排序只能用在数据范围不大的场景中，如果数据范围k比要排序的数据n大很多，就不适合用计数排序了
# 计数排序只能给非负整数排序，如果要排序的数据是其他类型的，要将其在不改变相对大小的情况下，转化为非负整数


def counting_sort(array):
    # 找出最大值
    max_value = max(array)
    # 初始化计数数组
    count_array = [0] * (max_value + 1)
    # 计数
    for i in array:
        count_array[i] += 1
    # 排序
    sorted_index = 0
    for i in range(max_value + 1):
        while count_array[i] > 0:
            array[sorted_index] = i
            sorted_index += 1
            count_array[i] -= 1
    return array

# test with 20 random numbers
import random

buf = [random.randint(0, 100) for _ in range(20)]
print(counting_sort(buf))
