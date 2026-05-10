from src.my_node import MyNode


def kth_to_last(head: MyNode, k: int) -> int:
    if head is None or k <= 0:
        return -1

    first = head
    second = head

    for _ in range(k):
        if second is None:
            return -1
        second = second.next

    while second is not None:
        first = first.next
        second = second.next

    return first.value