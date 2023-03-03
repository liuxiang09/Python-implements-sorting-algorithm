# 分而治之
# https://www.cnblogs.com/chengxiao/p/6194356.html

def merge(array, left, mid, right):
    _left = left
    _right = mid + 1
    index = 0
    temp = [None] * len(array)  # 开辟数组空间
    while _left <= mid and _right <= right:
        if array[_left] < array[_right]:  # 左边更小
            temp[index] = array[_left]
            _left += 1
            index += 1
        else:
            temp[index] = array[_right]
            _right += 1
            index += 1
    while _left <= mid:
        temp[index] = array[_left]
        _left += 1
        index += 1
    while _right <= right:
        temp[index] = array[_right]
        _right += 1
        index += 1

    # 将temp中的数据全部拷贝到原数组中
    index = 0
    for i in range(left, right + 1):
        array[i] = temp[index]
        index += 1
    return array


def merge_sort(array, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)
    return array


buf = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print(merge_sort(buf, 0, len(buf) - 1))
