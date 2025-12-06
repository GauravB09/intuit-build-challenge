import unittest
import time
import threading

from blocking_queue import BlockingQueue
from producer import Producer
from consumer import Consumer

class TestBlockingQueue(unittest.TestCase):

    def test_put_get_single_thread(self):
        # Basic check to see if put/get works in a simple list
        q = BlockingQueue(maxsize=2)
        q.put(1)
        q.put(2)
        self.assertTrue(q.full())
        self.assertEqual(q.get(), 1)
        self.assertEqual(q.get(), 2)
        self.assertTrue(q.empty())

    def test_producer_consumer_transfer(self):
        # Make sure all items get from producer to consumer
        src = [f"item-{i}" for i in range(20)]
        dst = []
        q = BlockingQueue(maxsize=5)
        sentinel = object()

        p = Producer(src, q, sentinel=sentinel)
        c = Consumer(q, dst, sentinel=sentinel)

        p.start()
        c.start()
        p.join()
        c.join()

        self.assertEqual(src, dst)

    def test_bounded_queue_blocks(self):
        # Queue size 1 should force the producer to wait
        src = list(range(50))
        dst = []
        q = BlockingQueue(maxsize=1)
        sentinel = object()

        # Add a tiny delay to consumer to ensure producer hits the full queue limit
        p = Producer(src, q, sentinel=sentinel)
        c = Consumer(q, dst, sentinel=sentinel, delay=0.001)

        p.start()
        c.start()
        p.join()
        c.join()

        self.assertEqual(src, dst)

    def test_empty_queue_blocks_consumer(self):
        # Consumer should wait if queue is empty (Wait/Notify check)
        q = BlockingQueue(maxsize=2)
        dst = []
        sentinel = -1

        def slow_producer():
            time.sleep(0.05)
            q.put(42)
            q.put(sentinel)

        t = threading.Thread(target=slow_producer)
        c = Consumer(q, dst, sentinel=sentinel)

        start = time.time()

        t.start()
        c.start()
        t.join()
        c.join()

        duration = time.time() - start

        self.assertEqual(dst, [42])
        # It must have waited at least 0.05s
        self.assertGreater(duration, 0.05)

    def test_unbounded_queue(self):
        # maxsize=0 should mean infinite size
        q = BlockingQueue(maxsize=0)
        self.assertFalse(q.full())

        for i in range(100):
            q.put(i)

        self.assertFalse(q.full())
        self.assertEqual(q.get(), 0)

    def test_bad_maxsize(self):
        # Negative size should fail
        with self.assertRaises(ValueError):
            BlockingQueue(maxsize=-1)

    def test_empty_input(self):
        # Shouldn't crash or hang if list is empty
        q = BlockingQueue(maxsize=5)
        sentinel = object()

        p = Producer([], q, sentinel=sentinel)
        c = Consumer(q, [], sentinel=sentinel)

        p.start()
        c.start()
        # Timeout prevents infinite hang if it fails
        p.join(timeout=1.0)
        c.join(timeout=1.0)

        self.assertFalse(p.is_alive())
        self.assertEqual([], [])

if __name__ == '__main__':
    unittest.main()