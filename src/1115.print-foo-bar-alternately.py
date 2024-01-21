#
# @lc app=leetcode id=1115 lang=python3
#
# [1115] Print FooBar Alternately
#

# @lc code=start
# TAGS: Concurrency
import threading
class FooBar:
    """Using primitive Locks"""
    def __init__(self, n):
        self.n = n
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock1.acquire()
            printFoo()
            self.lock2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock2.acquire()
            printBar()
            self.lock1.release()

import threading
class FooBar:
    """Using Condition"""
    def __init__(self, n):
        self.n = n
        self.state = "foo"
        self.condition = threading.Condition()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.state == "foo")
                printFoo()
                self.state = "bar"
                self.condition.notify_all()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.state == "bar")
                printBar()
                self.state = "foo"
                self.condition.notify_all()


import threading
class FooBar:
    """Using Barrier. Just be careful with the waiting order."""
    def __init__(self, n):
        self.n = n
        self.condition = threading.Barrier(2)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            printFoo()
            self.condition.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.condition.wait()
            printBar()
# @lc code=end

