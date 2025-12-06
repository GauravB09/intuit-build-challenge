import threading
import time
from typing import Any, Iterable

# Relative import for the shared resource
from blocking_queue import BlockingQueue

class Producer(threading.Thread):
    """
    Worker thread that moves data from a source to the BlockingQueue.
    """

    def __init__(
        self,
        source: Iterable[Any],
        queue: BlockingQueue,
        sentinel: Any = None,
        delay: float = 0.0,
    ):
        super().__init__()
        self.source = source
        self.queue = queue
        self.sentinel = sentinel
        self.delay = delay

    def run(self) -> None:
        for item in self.source:
            if self.delay > 0:
                time.sleep(self.delay)
            self.queue.put(item)

        # Signal completion
        if self.sentinel is not None:
            self.queue.put(self.sentinel)