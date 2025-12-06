import threading
from collections import deque
from typing import Any

class BlockingQueue:
    """
    A bounded blocking queue implemented with Condition variables.
    Handles thread-safe put/get operations using the Wait/Notify mechanism.
    """

    def __init__(self, maxsize: int = 0):
        if maxsize < 0:
            raise ValueError("maxsize must be >= 0")

        self._maxsize = maxsize
        self._queue = deque()
        self._lock = threading.Lock()

        # Condition variables for flow control (Wait/Notify)
        self._not_empty = threading.Condition(self._lock) # Consumers wait here
        self._not_full = threading.Condition(self._lock)  # Producers wait here

    def full(self) -> bool:
        """Return True if the queue is full, False otherwise."""
        if self._maxsize == 0:
            return False
        with self._lock:
            return len(self._queue) >= self._maxsize

    def empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        with self._lock:
            return len(self._queue) == 0

    def put(self, item: Any) -> None:
        """Put an item into the queue. Blocks if the queue is full."""
        with self._not_full:
            while self._maxsize > 0 and len(self._queue) >= self._maxsize:
                self._not_full.wait()

            self._queue.append(item)

            # Notify waiting consumers that data is available
            self._not_empty.notify()

    def get(self) -> Any:
        """Remove and return an item from the queue. Blocks if the queue is empty."""
        with self._not_empty:
            while not self._queue:
                self._not_empty.wait()

            item = self._queue.popleft()

            # Notify waiting producers that space is available
            self._not_full.notify()
            return item