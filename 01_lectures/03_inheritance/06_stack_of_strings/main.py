# from typing import Union
#
#
# class Stack:
#     def __init__(self):
#         self.data = []
#
#     def push(self, element) -> None:
#         self.data.append(element)
#
#     def pop(self) -> Union[str, None]:
#         return self.data.pop()
#
#     def top(self) -> str:
#         return self.data[-1]
#
#     def is_empty(self) -> bool:
#         return False if self.data else True
#
#     def __str__(self) -> str:
#         result = reversed(self.data)
#         return '[' + ', '.join([str(el) for el in result]) + ']'


class Stack:
    def __init__(self):
        self.data = []

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self) -> (str, None):
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return False if self.data else True

    def __str__(self) -> str:
        result = reversed(self.data)
        return '[' + ', '.join([str(el) for el in result]) + ']'


# class StackTests(unittest.TestCase):
#     def test_zero(self):
#         stack = Stack()
#         stack.push("apple")
#         stack.push("carrot")
#         self.assertEqual(str(stack), '[carrot, apple]')
#         self.assertEqual(stack.pop(), 'carrot')
#         self.assertEqual(stack.top(), 'apple')
#         stack.push("cucumber")
#         self.assertEqual(str(stack), '[cucumber, apple]')
#         self.assertEqual(stack.is_empty(), False)
#
#
# if __name__ == '__main__':
#     unittest.main()

s = Stack()
s.push('apple')
s.push('carrot')
print(s.data)
s.pop()
print(s.data)
s.top()
s.push('cucumber')
print(s.data)
print(s.is_empty())
