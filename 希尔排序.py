# 希尔排序算法
# 希尔排序思路

# 1. 选择一个增量序列 t1，t2，…，tk，其中 ti > tj, tk = 1；
# 2. 按增量序列个数 k，对序列进行 k 趟排序；
# 3. 每趟排序，根据对应的增量 ti，将待排序列分割成若干个长度为 m 的子序列，分别对各子表进行直接插入排序。仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

# 希尔增量序列
def shell_sort(alist):
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            i = j
            # 插入排序
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 2


# Hibbard增量序列
def shell_sort_hibbard(alist):
    n = len(alist)
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1
    while gap > 0:
        for j in range(gap, n):
            i = j
            # 插入排序
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        gap //= 3



if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Before sorting: ", li)
    shell_sort_hibbard(li)
    print("After sorting: ", li)