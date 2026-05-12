from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    stack = MyStack()

    for i in string:
        if i in "([{":
            stack.push(i)

        else:
            if stack.is_empty():
                return False

            top = stack.pop()

            if i == ")" and top != "(":
                return False

            if i == "]" and top != "[":
                return False

            if i == "}" and top != "{":
                return False

    return stack.is_empty()
