# 基数排序
# 将数组中的数按照个位排序、按照十位排序、按照百位排序……如此进行，当完成按照最大位数排序后，整个数组也就排序完成了
def radix_sort(array):
    # 获取数组中的最大值
    max_num = max(array)
    # 获取最大值的位数
    max_digit = len(str(max_num))
    # 基数排序
    for digit in range(max_digit):
        # 定义桶(大小为10)
        bucket_list = [[] for _ in range(10)]
        # 将数组中的元素放入桶中
        for num in array:
            # digit 从 0 开始
            # 个位数：num // 1 % 10；十位数：num // 10 % 10；百位数：num // 100 % 10
            bucket_list[num // (10 ** digit) % 10].append(num)
            # 将桶中的元素取出来，放回原数组中
        array.clear()
        for bucket in bucket_list:
            array.extend(bucket)
    return array


# test with 20 random numbers
import random

buf = [random.randint(0, 1000) for _ in range(20)]
print(radix_sort(buf))
