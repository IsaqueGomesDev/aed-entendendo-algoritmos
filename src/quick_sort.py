from src.my_array import MyArray


def quick_sort(array: MyArray) -> MyArray:

    quick(array, 0, len(array) - 1)

    return array


def quick(array: MyArray, low: int, high: int):

    if low < high:

        pivot_index = partition(array, low, high)

        quick(array, low, pivot_index - 1)

        quick(array, pivot_index + 1, high)


def partition(array: MyArray, low: int, high: int) -> int:

    pivot = array[high]

    i = low - 1

    for j in range(low, high):

        if array[j] <= pivot:

            i += 1

            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1
