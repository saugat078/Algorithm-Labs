
from linear_search import linear_search 
from binary_search import binary_search
import random
import time
import matplotlib.pyplot as plt

# generate random inputs
def generate_random_array(size):
    return [random.randint(0, 100000) for _ in range(size)]


def test_search_algorithm(search_algorithm, arr, x):
    start_time = time.time()
    index = search_algorithm(arr, x)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, index

# Generate arrays of different sizes and run the search algorithms on them
sizes = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

for size in sizes:
    arr = generate_random_array(size)
    x = random.choice(arr)
    
    # Test linear search
    linear_search_time, _ = test_search_algorithm(linear_search, arr, x)
    
    # Test binary search
    arr.sort()
    binary_search_time, _ = test_search_algorithm(binary_search, arr, x)
    
    # Print the execution times for the current array size
    print(f"Size: {size}")
    print(f"Linear search time: {linear_search_time:.6f} seconds")
    print(f"Binary search time: {binary_search_time:.6f} seconds\n")


linear_search_times = []
binary_search_times = []

for size in sizes:
    arr = generate_random_array(size)
    x = random.choice(arr)
    
    # Test linear search
    linear_search_time, _ = test_search_algorithm(linear_search, arr, x)
    linear_search_times.append(linear_search_time)
    
    # Test binary search
    arr.sort()
    binary_search_time, _ = test_search_algorithm(binary_search, arr, x)
    binary_search_times.append(binary_search_time)

# Plot the execution times
plt.plot(sizes, linear_search_times, label="Linear Search")
plt.plot(sizes, binary_search_times, label="Binary Search")
plt.xlabel("Input Size")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.show()

