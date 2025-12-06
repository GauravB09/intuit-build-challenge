# Intuit Build Challenge

## Overview
This repository contains solutions for the Intuit Build Challenge, implemented in Python.

---

## Assignment 1: Producer-Consumer Pattern
Implementation of a thread-safe Producer-Consumer pattern using manual synchronization (Wait/Notify).

### Files
* `Assignment 1/producer_consumer.py`: Core implementation of BlockingQueue, Producer, and Consumer.
* `Assignment 1/producer_consumer_test.py`: Comprehensive unit tests covering concurrency and edge cases.

### How to Run Tests
From the root directory, run the following command to execute all tests with verbose output:
```bash
python3 -m unittest discover -s 'Assignment 1' -p '*_test.py' -v
