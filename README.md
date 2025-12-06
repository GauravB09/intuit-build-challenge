# Intuit Build Challenge

## Overview
This repository contains solutions for the Intuit Build Challenge, implemented in Python.

---

## Assignment 1: Producer-Consumer Pattern
Implementation of a thread-safe Producer-Consumer pattern using manual synchronization (Wait/Notify).

Testing Objectives:
• Thread synchronization
• Concurrent programming
• Blocking queues
• Wait/Notify mechanism

Detailed Description: Implement a classic producer-consumer pattern demonstrating thread
synchronization and communication. The program will simulate concurrent data transfer
between a producer thread that reads from a source container and places items into a shared
queue, and a consumer thread that reads from the queue and stores items in a destination
container.

### Files
* `Assignment 1/blocking_queue.py`: Core implementation of BlockingQueue.
* `Assignment 1/consumer.py`: Core implementation of Consumer.
* `Assignment 1/producer.py`: Core implementation of Producer.
* `Assignment 1/producer_consumer_test.py`: Comprehensive unit tests covering concurrency and edge cases.

### How to Run Tests
From the root directory, run the following command to execute all tests with verbose output:
```bash
python3 -m unittest discover -s 'Assignment 1' -p '*_test.py' -v
```

---

## Assignment 2: Data Analysis on CSV File
Perform data analysis using appropriate API on CSV data.

Testing Objectives:
• Functional programming
• Stream operations
• Data aggregation
• Lambda expressions

Detailed Description: Develop a application that demonstrates proficiency with the Streams by
performing various aggregation and grouping operations on sales data provided in CSV format.
The program will read data from a CSV file and execute multiple analytical queries using
functional programming paradigms. Select or construct a CSV dataset that you feel best fits the
problem and document your choices and assumptions as part of your solution.

### Files
* `Assignment 2/stream_util.py`: Core implementation of Stream API.
* `Assignment 2/sales_analysis.py`: Main application performing data analysis.
* `Assignment 2/generate_sales_data.py`: Utility script to generate CSV datasets.
* `Assignment 2/sales_data.py`: Sample dataset used for analysis.
* `Assignment 2/sales_analysis_test.py`: Unit tests for sales analysis logic.
* `Assignment 2/stream_util_test.py`: Unit tests for the Stream utility class.

### How to Run Tests
From the root directory, run the following command to execute all tests with verbose output:

#### 1. Generate Sample Data Create a fresh sales_data.csv file with random records:
```bash
python3 'Assignment 2/generate_sales_data.py'
```

#### 2. Run Analysis Execute the main application to see the analysis report:
```bash
python3 'Assignment 2/sales_analysis.py'
```

#### 3. Run Tests Execute all unit tests with verbose output:
```bash
python3 -m unittest discover -s 'Assignment 2' -p '*_test.py' -v
```