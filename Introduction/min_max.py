def find_largest_and_smallest(arr):
    if not arr:  # Check if the list is empty
        return "Array is empty"
    
    largest = max(arr)
    smallest = min(arr)
    
    return largest, smallest

# Example usage
numbers = [4, 2, 9, 1, 5, 6]
largest, smallest = find_largest_and_smallest(numbers)
print(f"Largest: {largest}, Smallest: {smallest}")
