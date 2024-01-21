#
# @lc app=leetcode id=1116 lang=python3
#
# [1116] Print Zero Even Odd
#

# @lc code=start
# TAGS: Concurrency
import threading
class ZeroEvenOdd:
    """
    Using Condition Lock to simulate state machine
    0, 1 => 2
    2 => 1 if number is odd
    2 => 2 if number is even
    """
    def __init__(self, n):
        self.n = n
        self.order = 2
        self.condition = threading.Condition()
        
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        with self.condition:
            for i in range(1, self.n + 1):
                self.condition.wait_for(lambda: self.order == 2)
                printNumber(0)
                self.order = i % 2
                self.condition.notify_all()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        with self.condition:
            for i in range(2, self.n + 1, 2):
                self.condition.wait_for(lambda: self.order == 0)
                printNumber(i)
                self.order = 2
                self.condition.notify_all()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        with self.condition:
            for i in range(1, self.n + 1, 2):
                self.condition.wait_for(lambda: self.order == 1)
                printNumber(i)
                self.order = 2
                self.condition.notify_all()

import threading
class ZeroEvenOdd:
    """
    Using 3 primitive Locks
    
    From Docs: A primitive lock is in one of two states, “locked” or “unlocked”. It is created in the unlocked state. It has two basic methods, acquire() and release(). When the state is unlocked, acquire() changes the state to locked and returns immediately. When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked, then the acquire() call resets it to locked and returns. The release() method should only be called in the locked state; it changes the state to unlocked and returns immediately. If an attempt is made to release an unlocked lock, a RuntimeError will be raised.

    The exact same recipe can be used for threading.Semaphore(1) and Event()
    """
    def __init__(self, n):
        self.n = n
        self.odd_lock = threading.Lock()
        self.even_lock = threading.Lock()
        self.zero_lock = threading.Lock()
        self.odd_lock.acquire()
        self.even_lock.acquire()
        
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_lock.acquire()
            printNumber(0)
            if i % 2:
                self.odd_lock.release()
            else:
                self.even_lock.release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_lock.acquire()
            printNumber(i)
            self.zero_lock.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()

import threading
class ZeroEvenOdd:
    """
    Using 3 Event()
    """
    def __init__(self, n):
        self.n = n
        self.odd_lock = threading.Event()
        self.even_lock = threading.Event()
        self.zero_lock = threading.Event()
        self.zero_lock.set()
        
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_lock.wait()
            self.zero_lock.clear()
            printNumber(0)
            if i % 2:
                self.odd_lock.set()
            else:
                self.even_lock.set()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.even_lock.wait()
            self.even_lock.clear()
            printNumber(i)
            self.zero_lock.set()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_lock.wait()
            self.odd_lock.clear()
            printNumber(i)
            self.zero_lock.set()
        
        
# @lc code=end

