"""
Tests for Assignment 3: Data Structures
"""
import pytest
from data_structures import Stack, Queue, is_balanced


class TestStack:
    def test_push_and_peek(self):
        s = Stack()
        s.push(1)
        assert s.peek() == 1

    def test_pop_order(self):
        s = Stack()
        for v in [1, 2, 3]:
            s.push(v)
        assert s.pop() == 3
        assert s.pop() == 2

    def test_pop_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.pop()

    def test_peek_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.peek()

    def test_is_empty(self):
        s = Stack()
        assert s.is_empty()
        s.push(42)
        assert not s.is_empty()

    def test_size(self):
        s = Stack()
        for i in range(5):
            s.push(i)
        assert s.size() == 5


class TestQueue:
    def test_enqueue_and_front(self):
        q = Queue()
        q.enqueue("a")
        assert q.front() == "a"

    def test_dequeue_order(self):
        q = Queue()
        for v in ["x", "y", "z"]:
            q.enqueue(v)
        assert q.dequeue() == "x"
        assert q.dequeue() == "y"

    def test_dequeue_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.dequeue()

    def test_front_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.front()

    def test_size(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.size() == 2


class TestIsBalanced:
    @pytest.mark.parametrize("expr,expected", [
        ("([]{})", True),
        ("{[()]}", True),
        ("([)]", False),
        ("{", False),
        ("", True),
        ("hello world", True),
        ("(a + b) * [c - d]", True),
        ("((())", False),
    ])
    def test_balanced(self, expr, expected):
        assert is_balanced(expr) == expected
