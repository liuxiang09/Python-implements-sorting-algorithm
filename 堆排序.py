# https://www.jianshu.com/p/d174f1862601

def swap(array, start, end):
    array[start], array[end] = array[end], array[start]
    return array



def heap_adjust(array, start, end):  # 调整使得序列形成大顶堆
    i = 2 * start + 1  # 从0开始的数组，2i+1代表的是左子结点
    j = 2 * start + 2
    max_index = start
    if i <= end and array[max_index] < array[i]:
        max_index = i
    if j <= end and array[max_index] < array[j]:
        max_index = j
    if max_index is not start:  # 如果不等于则说明需要进行交换，还要继续递归进行
        array[start], array[max_index] = array[max_index], array[start]
        heap_adjust(array, max_index, end)
    return array


def heap_sort(array, start, end):    # 主函数，分为两部分：首先形成大顶堆，再把根取出，把某个叶子节点放到根位置，再次heap_adjust，以此类推。
    mid = end // 2
    for i in range(mid+1):    # 从中间开始（中间的那个位置是最后一个有子节点的位置），往start处倒序遍历一遍，形成大顶堆
        heap_adjust(array, mid-i, end)

    for i in range(1, end + 1):
        # 交换
        swap(array, start, end-i+1)
        heap_adjust(array, 0, end - i)  # 再次形成大顶堆，这时最大的数已经被拿出来了，所以需要把end减一

    return array


buf = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print(heap_sort(buf, 0, len(buf)-1))