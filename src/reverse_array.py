from src.my_array import MyArray


def reverse_array(array: MyArray) -> MyArray:

    for i in range(len(array) // 2):
        array[i], array[len(array) - 1 - i] = (
            array[len(array) - 1 - i],
            array[i]
        )
    return array
