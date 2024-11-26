from heapq import heapify  # Remove if not using heapq's heapify

def comparison(a, b):
    return a < b  # Simplified comparison

class Heap:
    '''
    Class to implement a heap with a general comparison function
    '''
    def __init__(self, comparison_function=comparison, init_array=[]):
        '''
        Initializes a heap with a comparison function and an optional initial array.
        '''
        self.comp = comparison_function
        self.array = init_array
        self.heapify(self.array)  # Use custom heapify logic
        
    def insert(self, value):
        '''
        Inserts a value into the heap.
        '''
        a = self.array
        a.append(value)  # Add the value to the end of the heap
        n = len(a)
        i = n - 1
        parent = (i - 1) // 2
        
        # Bubble up to maintain heap property
        while i > 0 and self.comp(a[i], a[parent]):
            a[i], a[parent] = a[parent], a[i]
            i = parent
            parent = (i - 1) // 2
    
    def extract(self):
        '''
        Extracts the top value from the heap.
        '''
        a = self.array
        if len(a) == 0:
            return None  # Heap is empty
        
        # Swap the first and last element, then remove the last
        top_value = a[0]
        last_value = a.pop()
        
        if len(a) > 0:
            a[0] = last_value  # Place the last value at the root
            self.heap(a, len(a), 0)  # Restore heap property from the root
        
        return top_value
    
    def top(self):
        '''
        Returns the top value of the heap without removing it.
        '''
        if len(self.array) > 0:
            return self.array[0]
        return None
    
    def heap(self, arr, n, i):
        '''
        Heapifies a subtree rooted at index `i` for an array `arr` of size `n`.
        '''
        mini = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        # Check if the left child is smaller
        if left < n and self.comp(arr[left], arr[mini]):
            mini = left
        
        # Check if the right child is smaller
        if right < n and self.comp(arr[right], arr[mini]):
            mini = right
        
        # If the smallest is not the current node
        if mini != i:
            arr[i], arr[mini] = arr[mini], arr[i]  # Swap
            self.heap(arr, n, mini)  # Recursively heapify the affected subtree
    
    def heapify(self, arr):
        '''
        Turns an array into a heap by heapifying all non-leaf nodes.
        '''
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heap(arr, n, i)
