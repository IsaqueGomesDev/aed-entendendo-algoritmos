from src.my_node import MyNode


def remove_duplicates(head: MyNode) -> MyNode:
    current = head

    while current is not None:
        runner = current
        while runner.next is not None:
            if current.value == runner.next.value:
                runner.next = runner.next.next     
            else:
                runner = runner.next     
        current = current.next
    return head