"""
Assignment 3: Data Structures — Lists, Stacks, and Queues
ITP2 | SE-2057 | Arnur & Marat
"""
from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """LIFO stack implemented with a Python list."""

    def __init__(self):
        self._data: list = []

    def push(self, item: T) -> None:
        self._data.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Pop from an empty stack.")
        return self._data.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Peek on an empty stack.")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data!r})"


class Queue(Generic[T]):
    """FIFO queue implemented with a Python list."""

    def __init__(self):
        self._data: list = []

    def enqueue(self, item: T) -> None:
        self._data.append(item)

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue.")
        # Note: pop(0) is O(n); use collections.deque for O(1) in production.
        return self._data.pop(0)

    def front(self) -> T:
        if self.is_empty():
            raise IndexError("Front on an empty queue.")
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({self._data!r})"


def is_balanced(expression: str) -> bool:
    """Check whether brackets in expression are balanced.

    Supported bracket pairs: (), [], {}
    """
    matching = {")": "(", "]": "[", "}": "{"}
    stack: Stack = Stack()

    for ch in expression:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.is_empty() or stack.pop() != matching[ch]:
                return False

    return stack.is_empty()


def main():
    print("=== Stack Demo ===")
    s: Stack = Stack()
    for val in [1, 2, 3]:
        s.push(val)
    print(f"Stack: {s}")
    print(f"Peek : {s.peek()}")
    print(f"Pop  : {s.pop()}")
    print(f"Stack after pop: {s}")

    print("\n=== Queue Demo ===")
    q: Queue = Queue()
    for val in ["a", "b", "c"]:
        q.enqueue(val)
    print(f"Queue : {q}")
    print(f"Front : {q.front()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Queue after dequeue: {q}")

    print("\n=== Balanced Brackets ===")
    tests = [
        ("([]{})", True),
        ("{[()]}", True),
        ("([)]", False),
        ("{", False),
        ("", True),
    ]
    for expr, expected in tests:
        result = is_balanced(expr)
        status = "✓" if result == expected else "✗"
        print(f"  {status} is_balanced({expr!r}) = {result}")


if __name__ == "__main__":
    main()
