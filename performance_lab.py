# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    frequency = {}
    max_count = 0
    most_common = None

    for num in numbers: 
        frequency[num] = frequency.get(num, 0) + 1
        if frequency[num] > max_count:
            max_count = frequency[num]
            most_common = num
    return most_common


print(most_frequent([1, 3, 2, 3, 4, 1, 3]))

"""
Time and Space Analysis for problem 1:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach?
- Could it be optimized? I don't think so. It's already optimal for most cases.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
    
print(remove_duplicates([4, 5, 4, 6, 5, 7]))

"""
Time and Space Analysis for problem 2:
- Best-case:O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? This way it keeps the order of the list but makes the changes neccessary to remove dupes
- Could it be optimized? Not really. To keep the order the list needs to be scanned. 
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs) 

print(find_pairs([1, 2, 3, 4], 5))

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? This avoids nested loops which would add time
- Could it be optimized? It's already optimal for this type of list. 
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    lst = [None] * capacity
    size = 0

    for i in range(n):
        if size == capacity:
            capacity *= 2
            print(f"Resizing to capacity: {capacity}")
            new_lst = [None] * capacity
            for j in range(size):
                new_lst[j] = lst[j]
            lst = new_lst
        lst[size] = i
        size += 1
add_n_items(6)
"""
Time and Space Analysis for problem 4:
- When do resizes happen? When the size reaches capacity
- What is the worst-case for a single append? O(n) during resizing
- What is the amortized time per append overall? O(1)
- Space complexity: O(n)
- Why does doubling reduce the cost overall? Because of doubling it cuts down the amount of times it has to resize. 
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    total = 0
    result = []
    for num in nums:
        total += num
        result.append(total)
    return result 

print(running_total([1, 2, 3, 4]))

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: 0(n)
- Average-case: O(n)
- Space complexity: O(n)
- Why this approach? It's a simple one pass compute. 
- Could it be optimized? Already opimtal. 
"""
