arr_list = [3, 4, 6, 1, 5, 10, 8, 7, 9]


def quick_sort(arr: list):
    left = []
    right = []
    middle = []
    if len(arr) < 2:
        return arr
    else:
        mid = arr[0]
        for i in arr:
            if i > mid:
                right.append(i)
            elif i == mid:
                middle.append(i)
            else:
                left.append(i)
        less = quick_sort(left)
        right = quick_sort(right)
        return less + middle + right


print(quick_sort(arr_list))
