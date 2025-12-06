import threading
import time
from typing import Any, List

from blocking_queue import BlockingQueue

class Consumer(threading.Thread):
    """
    Worker thread that moves data from the BlockingQueue to a destination.
    Stops when it encounters the sentinel value.
    """

    def __init__(
        self,
        queue: BlockingQueue,
        destination: List[Any],
        sentinel: Any = None,
        delay: float = 0.0,
    ):
        super().__init__()
        self.queue = queue
        self.destination = destination
        self.sentinel = sentinel
        self.delay = delay

    def run(self) -> None:
        while True:
            item = self.queue.get()
            if item == self.sentinel:
                break

            if self.delay > 0:
                time.sleep(self.delay)
            self.destination.append(item)