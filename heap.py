import random
import timeit
import matplotlib.pyplot as plt

# Function to heapify a subtree rooted at index i
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Check if left child exists and is greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # Check if right child exists and is greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        # Heapify the root
        heapify(arr, n, largest)

# Main function to perform heap sort
def heapSort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Input array size from the user
array_size = int(input("Enter the size of the input array: "))

# Generate random arrays and measure execution times
input_sizes = list(range(1, array_size + 1))
execution_times = []

for size in input_sizes:
    input_array = [random.randint(1, 1000) for _ in range(size)]
    start_time = timeit.default_timer()
    heapSort(input_array)
    end_time = timeit.default_timer()
    execution_times.append(end_time - start_time)

# Plot the graph
plt.plot(input_sizes, execution_times, marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Input Size vs. Execution Time')
plt.show()
