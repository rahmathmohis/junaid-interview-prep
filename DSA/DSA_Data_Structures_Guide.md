# Data Structures & Algorithms - Complete Guide

## Interview Preparation Guide for Campus Placement
**Dayanand Sagar Engineering - 4th Year**

---

## 📑 Table of Contents

**Legend:** 🟢 Easy | 🟡 Medium | 🔴 Hard

### CORE CONCEPTS & BASICS
- [🟢 Data Types & Typing Systems Interview Guide](./Data_Types_Interview_Notes.md)

### DATA STRUCTURES (20 topics)
1. [🟢 Arrays](#1-arrays)
2. [🟢 Linked Lists](#2-linked-lists)
3. [🟢 Stacks](#3-stacks)
4. [🟢 Queues](#4-queues)
5. [🟡 Hash Tables](#5-hash-tables)
6. [🟡 Trees (Binary Trees)](#6-trees-binary-trees)
7. [🟡 Binary Search Trees](#7-binary-search-trees)
8. [🔴 AVL Trees](#8-avl-trees)
9. [🟡 Heaps](#9-heaps)
10. [🔴 Graphs](#10-graphs)
11. [🔴 Tries](#11-tries)
12. [🟡 Priority Queues](#12-priority-queues)

### ALGORITHMS (20 topics)
13. [🟢 Searching (Linear, Binary)](#13-searching-algorithms)
14. [🟡 Sorting (Bubble, Selection, Insertion)](#14-basic-sorting-algorithms)
15. [🟡 Advanced Sorting (Merge, Quick, Heap)](#15-advanced-sorting-algorithms)
16. [🟡 Recursion](#16-recursion)
17. [🟡 Backtracking](#17-backtracking)
18. [🔴 Dynamic Programming](#18-dynamic-programming)
19. [🔴 Greedy Algorithms](#19-greedy-algorithms)
20. [🔴 Divide and Conquer](#20-divide-and-conquer)
21. [🟡 Two Pointers](#21-two-pointers-technique)
22. [🟡 Sliding Window](#22-sliding-window)
23. [🟡 BFS and DFS](#23-bfs-and-dfs)
24. [🔴 Dijkstra's Algorithm](#24-dijkstras-algorithm)
25. [🔴 Bellman-Ford](#25-bellman-ford)
26. [🔴 Floyd-Warshall](#26-floyd-warshall)
27. [🟡 Topological Sort](#27-topological-sort)
28. [🔴 Minimum Spanning Tree](#28-minimum-spanning-tree)

### Quick Reference
- [⏰ Time Complexity Cheat Sheet](#-time-complexity-cheat-sheet)
- [📊 When to Use Which Data Structure](#-when-to-use-which-data-structure)
- [🎯 Top Problem Patterns](#-top-problem-patterns)

---

## DATA STRUCTURES

### 1. Arrays 🟢

**Definition:**
Contiguous memory allocation storing elements of the same type with constant-time index access.

**Time Complexity:**
- Access: O(1)
- Search: O(n)
- Insert: O(n)
- Delete: O(n)

**Python Implementation:**
```python
# Array operations
arr = [1, 2, 3, 4, 5]

# Access - O(1)
first = arr[0]
last = arr[-1]

# Search - O(n)
if 3 in arr:
    index = arr.index(3)

# Insert - O(n) - shifts all elements
arr.insert(2, 99)  # Insert 99 at index 2

# Delete - O(n)
arr.remove(99)     # Remove by value
arr.pop(2)         # Remove by index

# Common operations
arr.append(6)      # O(1) amortized
arr.extend([7, 8]) # O(k) where k is length
arr.sort()         # O(n log n)
arr.reverse()      # O(n)

# Slicing
subarray = arr[1:4]  # O(k) where k is slice length

# 2D Arrays
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element
element = matrix[1][2]  # 6

# Traverse
for row in matrix:
    for elem in row:
        print(elem)
```

**Common Problems:**
```python
# 1. Find maximum element
def find_max(arr):
    return max(arr)  # O(n)

# 2. Reverse array in-place
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# 3. Rotate array by k positions
def rotate_array(arr, k):
    k = k % len(arr)
    arr[:] = arr[-k:] + arr[:-k]

# 4. Find duplicates
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)
```

**Key Takeaway:**
Arrays provide O(1) access but O(n) insertion/deletion. Best for fixed-size collections with frequent access.

---

### 2. Linked Lists 🟢

**Definition:**
Linear data structure where elements (nodes) are connected via pointers/references. Each node contains data and reference to next node.

**Types:**
1. **Singly Linked List**: One pointer (next)
2. **Doubly Linked List**: Two pointers (next, prev)
3. **Circular Linked List**: Last node points to first

**Time Complexity:**
- Access: O(n)
- Search: O(n)
- Insert at head: O(1)
- Delete at head: O(1)
- Insert at tail: O(n) or O(1) with tail pointer

**Python Implementation:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insert at beginning - O(1)
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Insert at end - O(n)
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    # Delete node - O(n)
    def delete(self, data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    # Search - O(n)
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    # Display - O(n)
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    # Reverse linked list - O(n)
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    # Find middle element - O(n) using slow/fast pointers
    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None
    
    # Detect cycle - O(n)
    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Usage
ll = LinkedList()
ll.insert_at_head(3)
ll.insert_at_head(2)
ll.insert_at_head(1)
ll.insert_at_tail(4)
print(ll.display())  # [1, 2, 3, 4]
```

**Doubly Linked List:**
```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, data):
        new_node = DNode(data)
        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
```

**Key Takeaway:**
Linked lists excel at O(1) insertion/deletion at head but have O(n) access. No memory waste, dynamic size.

---

### 3. Stacks 🟢

**Definition:**
LIFO (Last In First Out) data structure. Elements added/removed from top only.

**Time Complexity:**
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Search: O(n)

**Python Implementation:**
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)  # O(1)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # O(1)
        raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def size(self):
        return len(self.items)

# Using Python list as stack
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
top = stack.pop()  # Pop - returns 3
peek = stack[-1]   # Peek - returns 2

# Using collections.deque (more efficient)
from collections import deque
stack = deque()
stack.append(1)     # Push
stack.pop()         # Pop
```

**Common Applications:**
```python
# 1. Balanced Parentheses
def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != pairs[char]:
                return False
    
    return len(stack) == 0

print(is_balanced("({[]})"))  # True
print(is_balanced("({[}])"))  # False

# 2. Reverse string
def reverse_string(s):
    stack = list(s)
    return ''.join(stack[::-1])

# 3. Evaluate postfix expression
def evaluate_postfix(expression):
    stack = []
    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a // b)
    return stack.pop()

print(evaluate_postfix("3 4 + 2 *"))  # (3+4)*2 = 14

# 4. Next Greater Element
def next_greater_element(arr):
    result = [-1] * len(arr)
    stack = []
    
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    
    return result

print(next_greater_element([4, 5, 2, 10, 8]))
# [5, 10, 10, -1, -1]
```

**Key Takeaway:**
Stacks provide LIFO access with O(1) operations. Used for function calls, undo operations, parsing, backtracking.

---

### 4. Queues 🟢

**Definition:**
FIFO (First In First Out) data structure. Elements added at rear, removed from front.

**Types:**
1. **Simple Queue**: Basic FIFO
2. **Circular Queue**: Last position connects to first
3. **Priority Queue**: Elements have priorities
4. **Deque (Double-ended Queue)**: Insert/delete at both ends

**Time Complexity:**
- Enqueue: O(1)
- Dequeue: O(1)
- Front: O(1)

**Python Implementation:**
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)  # O(1)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()  # O(1)
        raise IndexError("Queue is empty")
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empty")
    
    def size(self):
        return len(self.items)

# Usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1 (FIFO)

# Using collections.deque directly
queue = deque()
queue.append(1)      # Enqueue
queue.append(2)
front = queue.popleft()  # Dequeue - returns 1
```

**Circular Queue:**
```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")
        
        if self.front == -1:
            self.front = 0
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
```

**Common Applications:**
```python
# 1. BFS traversal
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# 2. Level-order traversal of binary tree
def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

**Key Takeaway:**
Queues provide FIFO access with O(1) operations. Essential for BFS, task scheduling, buffering.

---

### 5. Hash Tables 🟡

**Definition:**
Hash table (dictionary in Python) stores key-value pairs with O(1) average lookup time. Uses hash function to compute index where value is stored.

**Time Complexity:**
- Access: N/A
- Search: O(1) average, O(n) worst
- Insert: O(1) average
- Delete: O(1) average

**Python Implementation:**
```python
# Dictionary operations - Python's built-in hash table
hash_map = {}

# Insert/Update - O(1)
hash_map["name"] = "Alice"
hash_map["age"] = 25
hash_map.update({"city": "NYC", "job": "Engineer"})

# Search - O(1)
if "name" in hash_map:
    print(hash_map["name"])

# Delete - O(1)
del hash_map["age"]
value = hash_map.pop("city", None)  # Returns None if not found

# Iteration
for key, value in hash_map.items():
    print(f"{key}: {value}")

# Common operations
keys = list(hash_map.keys())
values = list(hash_map.values())

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
```

**Collision Handling:**
```python
# Python handles collisions internally, but concept:
# 1. Chaining - linked list at each index
# 2. Open addressing - find next available slot

# Custom hash table implementation
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        # Chaining: store multiple items at same index
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

# Usage
ht = HashTable()
ht.insert("apple", 10)
ht.insert("banana", 20)
print(ht.get("apple"))  # 10
```

**Common Problems:**
```python
# 1. Two Sum
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]

# 2. First non-repeating character
def first_unique_char(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

# 3. Group anagrams
def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        anagrams.setdefault(key, []).append(word)
    return list(anagrams.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

**Key Takeaway:**
Hash tables provide O(1) average-case operations for key lookups, making them ideal for caching, counting, and fast retrieval.

---

### 6. Trees (Binary Trees) 🟡

**Definition:**
A tree is a hierarchical data structure with nodes connected by edges. Binary tree: each node has at most two children (left and right).

**Types:**
1. **Full Binary Tree**: Every node has 0 or 2 children
2. **Complete Binary Tree**: All levels filled except possibly last
3. **Perfect Binary Tree**: All internal nodes have 2 children, all leaves at same level
4. **Balanced Binary Tree**: Height difference between left and right subtrees ≤ 1

**Time Complexity:**
- Search: O(n)
- Insert: O(n)
- Delete: O(n)

**Python Implementation:**
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    # Traversal methods
    def inorder(self, node, result=[]):
        # Left -> Root -> Right
        if node:
            self.inorder(node.left, result)
            result.append(node.val)
            self.inorder(node.right, result)
        return result
    
    def preorder(self, node, result=[]):
        # Root -> Left -> Right
        if node:
            result.append(node.val)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        return result
    
    def postorder(self, node, result=[]):
        # Left -> Right -> Root
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.val)
        return result
    
    def level_order(self, root):
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            level = []
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        return result
    
    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def is_balanced(self, node):
        if not node:
            return True
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        return self.is_balanced(node.left) and self.is_balanced(node.right)

# Create tree:     1
#                 / \
#                2   3
#               / \
#              4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

tree = BinaryTree()
print(tree.inorder(root, []))      # [4, 2, 5, 1, 3]
print(tree.preorder(root, []))     # [1, 2, 4, 5, 3]
print(tree.postorder(root, []))    # [4, 5, 2, 3, 1]
print(tree.level_order(root))      # [[1], [2, 3], [4, 5]]
```

**Common Problems:**
```python
# 1. Maximum depth
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# 2. Check if tree is symmetric
def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    return is_mirror(root, root) if root else True

# 3. Lowest common ancestor
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    
    if left and right:
        return root
    return left if left else right
```

**Key Takeaway:**
Binary trees are hierarchical structures with various traversal methods (inorder, preorder, postorder, level-order) - each useful for different problems.

---

### 7. Binary Search Trees 🟡

**Definition:**
BST is a binary tree where left child < parent < right child. This property enables efficient searching, insertion, and deletion.

**Time Complexity:**
- Search: O(log n) average, O(n) worst
- Insert: O(log n) average, O(n) worst
- Delete: O(log n) average, O(n) worst

**Python Implementation:**
```python
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = BSTNode(val)
        else:
            self._insert_helper(self.root, val)
    
    def _insert_helper(self, node, val):
        if val < node.val:
            if node.left:
                self._insert_helper(node.left, val)
            else:
                node.left = BSTNode(val)
        else:
            if node.right:
                self._insert_helper(node.right, val)
            else:
                node.right = BSTNode(val)
    
    def search(self, val):
        return self._search_helper(self.root, val)
    
    def _search_helper(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._search_helper(node.left, val)
        else:
            return self._search_helper(node.right, val)
    
    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def delete(self, val):
        self.root = self._delete_helper(self.root, val)
    
    def _delete_helper(self, node, val):
        if not node:
            return None
        
        if val < node.val:
            node.left = self._delete_helper(node.left, val)
        elif val > node.val:
            node.right = self._delete_helper(node.right, val)
        else:
            # Node with one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children: get inorder successor
            min_node = self.find_min(node.right)
            node.val = min_node.val
            node.right = self._delete_helper(node.right, min_node.val)
        
        return node
    
    def inorder(self, node, result=[]):
        if node:
            self.inorder(node.left, result)
            result.append(node.val)
            self.inorder(node.right, result)
        return result

# Usage
bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

print(bst.search(40))  # True
print(bst.inorder(bst.root, []))  # [20, 30, 40, 50, 60, 70, 80]
bst.delete(30)
```

**Common Problems:**
```python
# 1. Validate BST
def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    
    if root.val <= min_val or root.val >= max_val:
        return False
    
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))

# 2. Kth smallest element
def kth_smallest(root, k):
    stack = []
    current = root
    count = 0
    
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            count += 1
            if count == k:
                return current.val
            current = current.right
        else:
            break
```

**Key Takeaway:**
BST maintains sorted order with O(log n) operations when balanced. Inorder traversal gives sorted sequence.

---

### 8. AVL Trees 🔴

**Definition:**
AVL tree is a self-balancing BST where height difference between left and right subtrees (balance factor) is at most 1. Ensures O(log n) operations.

**Balance Factor:** height(left subtree) - height(right subtree) ∈ {-1, 0, 1}

**Rotations:**
1. **Left Rotation**: Fix right-heavy tree
2. **Right Rotation**: Fix left-heavy tree
3. **Left-Right Rotation**: Left rotate child, then right rotate parent
4. **Right-Left Rotation**: Right rotate child, then left rotate parent

**Python Implementation:**
```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0
    
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0
    
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
    
    def insert(self, node, val):
        # Step 1: Normal BST insertion
        if not node:
            return AVLNode(val)
        
        if val < node.val:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)
        
        # Step 2: Update height
        node.height = 1 + max(self.get_height(node.left), 
                              self.get_height(node.right))
        
        # Step 3: Get balance factor
        balance = self.get_balance(node)
        
        # Step 4: Balance the tree
        # Left Left Case
        if balance > 1 and val < node.left.val:
            return self.right_rotate(node)
        
        # Right Right Case
        if balance < -1 and val > node.right.val:
            return self.left_rotate(node)
        
        # Left Right Case
        if balance > 1 and val > node.left.val:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        # Right Left Case
        if balance < -1 and val < node.right.val:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
        return node

# Usage
avl = AVLTree()
root = None
for val in [10, 20, 30, 40, 50, 25]:
    root = avl.insert(root, val)
```

**Key Takeaway:**
AVL trees maintain balance through rotations, guaranteeing O(log n) operations even in worst case.

---

### 9. Heaps 🟡

**Definition:**
Heap is a complete binary tree satisfying heap property:
- **Max Heap**: Parent ≥ children
- **Min Heap**: Parent ≤ children

**Time Complexity:**
- Find Min/Max: O(1)
- Insert: O(log n)
- Delete Min/Max: O(log n)
- Heapify: O(n)

**Python Implementation:**
```python
import heapq

# Python's heapq implements min heap

# Create heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
heapq.heappush(heap, 1)

print(heap)  # [1, 3, 7, 5] - internal representation

# Get minimum (doesn't remove)
print(heap[0])  # 1

# Pop minimum
min_val = heapq.heappop(heap)  # 1
print(heap)  # [3, 5, 7]

# Heapify existing list
nums = [5, 7, 2, 8, 1, 9]
heapq.heapify(nums)  # O(n)
print(nums)  # [1, 5, 2, 8, 7, 9]

# Max heap (negate values)
max_heap = []
for num in [5, 3, 7, 1]:
    heapq.heappush(max_heap, -num)

max_val = -heapq.heappop(max_heap)  # 7

# K largest elements
nums = [1, 23, 12, 9, 30, 2, 50]
k_largest = heapq.nlargest(3, nums)  # [50, 30, 23]
k_smallest = heapq.nsmallest(3, nums)  # [1, 2, 9]

# Custom heap with objects
class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    
    def __lt__(self, other):
        return self.priority < other.priority

task_heap = []
heapq.heappush(task_heap, Task(3, "Low priority"))
heapq.heappush(task_heap, Task(1, "High priority"))
heapq.heappush(task_heap, Task(2, "Medium priority"))

while task_heap:
    task = heapq.heappop(task_heap)
    print(f"{task.name}: {task.priority}")
```

**Common Problems:**
```python
# 1. Kth largest element
def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# 2. Merge K sorted lists
def merge_k_sorted(lists):
    heap = []
    result = []
    
    # Add first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result

# 3. Top K frequent elements
def top_k_frequent(nums, k):
    from collections import Counter
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
```

**Key Takeaway:**
Heaps provide O(1) access to min/max and O(log n) insertion/deletion. Perfect for priority queues and finding K largest/smallest elements.

---

### 10. Graphs 🔴

**Definition:**
Graph is a collection of nodes (vertices) connected by edges. Can be directed or undirected, weighted or unweighted.

**Representations:**
1. **Adjacency Matrix**: 2D array, O(V²) space
2. **Adjacency List**: Dictionary of lists, O(V + E) space

**Python Implementation:**
```python
# Adjacency List (most common)
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, v1, v2, directed=False):
        if v1 not in self.graph:
            self.add_vertex(v1)
        if v2 not in self.graph:
            self.add_vertex(v2)
        
        self.graph[v1].append(v2)
        if not directed:
            self.graph[v2].append(v1)
    
    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

# Create graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.display()
# 0: [1, 2]
# 1: [0, 2]
# 2: [0, 1, 3]
# 3: [2]

# Weighted graph
class WeightedGraph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, v1, v2, weight):
        if v1 not in self.graph:
            self.graph[v1] = []
        self.graph[v1].append((v2, weight))

wg = WeightedGraph()
wg.add_edge('A', 'B', 4)
wg.add_edge('A', 'C', 2)
wg.add_edge('B', 'C', 1)
```

**Graph Traversal:**
```python
from collections import deque

# DFS - Depth First Search
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited

# BFS - Breadth First Search
def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS:", end=' ')
dfs(graph, 'A')  # A B D E F C
print("\nBFS:", bfs(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
```

**Common Problems:**
```python
# 1. Detect cycle in undirected graph
def has_cycle(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

# 2. Number of connected components
def count_components(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    count = 0
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1
    
    return count

# 3. Is graph bipartite?
def is_bipartite(graph):
    color = {}
    
    def dfs(node, c):
        color[node] = c
        for neighbor in graph.get(node, []):
            if neighbor not in color:
                if not dfs(neighbor, 1 - c):
                    return False
            elif color[neighbor] == c:
                return False
        return True
    
    for node in graph:
        if node not in color:
            if not dfs(node, 0):
                return False
    return True
```

**Key Takeaway:**
Graphs model relationships between entities. Use adjacency list for sparse graphs, DFS for path-finding, BFS for shortest path in unweighted graphs.

---

### 11. Tries 🔴

**Definition:**
Trie (prefix tree) is a tree-like data structure for storing strings. Each node represents a character, enabling efficient prefix-based operations.

**Time Complexity:**
- Insert: O(m) where m is string length
- Search: O(m)
- StartsWith: O(m)

**Python Implementation:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            child_node = node.children[char]
            should_delete = _delete(child_node, word, index + 1)
            
            if should_delete:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        _delete(self.root, word, 0)
    
    def get_all_words(self):
        words = []
        def dfs(node, current_word):
            if node.is_end_of_word:
                words.append(current_word)
            
            for char, child_node in node.children.items():
                dfs(child_node, current_word + char)
        
        dfs(self.root, "")
        return words
    
    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        words = []
        def dfs(node, current):
            if node.is_end_of_word:
                words.append(prefix + current)
            for char, child_node in node.children.items():
                dfs(child_node, current + char)
        
        dfs(node, "")
        return words

# Usage
trie = Trie()
words = ["apple", "app", "application", "apply", "banana", "band"]
for word in words:
    trie.insert(word)

print(trie.search("app"))           # True
print(trie.search("appl"))          # False
print(trie.starts_with("app"))      # True
print(trie.autocomplete("app"))     # ['apple', 'application', 'apply', 'app']
print(trie.get_all_words())         # All inserted words
```

**Common Problems:**
```python
# 1. Longest common prefix
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    trie = Trie()
    for s in strs:
        trie.insert(s)
    
    node = trie.root
    prefix = ""
    
    while len(node.children) == 1 and not node.is_end_of_word:
        char = list(node.children.keys())[0]
        prefix += char
        node = node.children[char]
    
    return prefix

# 2. Word search in 2D board
def word_search(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    # Use trie to efficiently search multiple words
    # Implementation omitted for brevity
    pass
```

**Key Takeaway:**
Tries excel at prefix-based operations, autocomplete, and searching multiple strings efficiently. Used in spell checkers and search engines.

---

### 12. Priority Queues 🟡

**Definition:**
Priority queue is an abstract data type where each element has a priority. Elements with higher priority are served before lower priority. Implemented using heaps.

**Python Implementation:**
```python
import heapq
from queue import PriorityQueue

# Method 1: Using heapq (min heap)
class PriorityQueueHeap:
    def __init__(self):
        self.heap = []
        self.index = 0
    
    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, self.index, item))
        self.index += 1
    
    def pop(self):
        return heapq.heappop(self.heap)[2]
    
    def is_empty(self):
        return len(self.heap) == 0

# Usage
pq = PriorityQueueHeap()
pq.push("task1", 3)
pq.push("task2", 1)
pq.push("task3", 2)

while not pq.is_empty():
    print(pq.pop())  # task2, task3, task1

# Method 2: Using queue.PriorityQueue
pq2 = PriorityQueue()
pq2.put((2, "medium priority"))
pq2.put((1, "high priority"))
pq2.put((3, "low priority"))

while not pq2.empty():
    priority, item = pq2.get()
    print(item)  # high, medium, low

# Custom priority queue for max heap
class MaxPriorityQueue:
    def __init__(self):
        self.heap = []
    
    def push(self, item, priority):
        heapq.heappush(self.heap, (-priority, item))
    
    def pop(self):
        return heapq.heappop(self.heap)[1]

max_pq = MaxPriorityQueue()
max_pq.push("low", 1)
max_pq.push("high", 10)
max_pq.push("medium", 5)

print(max_pq.pop())  # high
```

**Key Takeaway:**
Priority queues serve elements based on priority, not insertion order. Essential for scheduling, shortest path algorithms, and event-driven simulations.

---

## ALGORITHMS

### 13. Searching Algorithms 🟢

**Definition:**
Searching algorithms find the position of a target element in a data structure.

**1. Linear Search:**
- Check each element sequentially
- Time: O(n), Space: O(1)

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([5, 3, 7, 1, 9], 7))  # 2
```

**2. Binary Search:**
- Requires sorted array
- Divide array in half repeatedly
- Time: O(log n), Space: O(1)

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Recursive version
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))  # 3
```

**Key Takeaway:**
Binary search is O(log n) but requires sorted data. Linear search works on unsorted data but is O(n).

---

### 14. Basic Sorting Algorithms 🟡

**1. Bubble Sort:**
- Repeatedly swap adjacent elements if in wrong order
- Time: O(n²), Space: O(1)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
```

**2. Selection Sort:**
- Find minimum and place at beginning
- Time: O(n²), Space: O(1)

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))
```

**3. Insertion Sort:**
- Build sorted array one element at a time
- Time: O(n²) worst, O(n) best, Space: O(1)

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([12, 11, 13, 5, 6]))
```

**Key Takeaway:**
Basic sorts are O(n²) but simple and efficient for small datasets. Insertion sort is adaptive.

---

### 15. Advanced Sorting Algorithms 🟡

**1. Merge Sort:**
- Divide and conquer
- Time: O(n log n), Space: O(n)

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
```

**2. Quick Sort:**
- Divide and conquer with pivot
- Time: O(n log n) average, O(n²) worst, Space: O(log n)

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# In-place version
def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [10, 7, 8, 9, 1, 5]
quick_sort_inplace(arr, 0, len(arr) - 1)
print(arr)
```

**3. Heap Sort:**
- Uses heap data structure
- Time: O(n log n), Space: O(1)

```python
def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

print(heap_sort([12, 11, 13, 5, 6, 7]))
```

**Key Takeaway:**
Advanced sorts are O(n log n). Merge sort is stable, quick sort is fast in practice, heap sort uses O(1) space.

---

### 16. Recursion 🟡

**Definition:**
Function that calls itself with smaller input until reaching base case.

```python
# Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Power
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# Reverse string
def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])

print(factorial(5))  # 120
print(fibonacci(7))  # 13
print(reverse_string("hello"))  # olleh
```

**Key Takeaway:**
Recursion needs base case and recursive case. Can be elegant but watch for stack overflow.

---

### 17. Backtracking 🟡

**Definition:**
Algorithmic technique that tries all possibilities and backtracks when a path fails.

```python
# N-Queens problem
def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 1:
                return False
        
        # Check diagonals
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 1:
                return False
        
        return True
    
    def solve(board, row):
        if row >= n:
            return True
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                
                if solve(board, row + 1):
                    return True
                
                board[row][col] = 0  # Backtrack
        
        return False
    
    board = [[0] * n for _ in range(n)]
    solve(board, 0)
    return board

# Sudoku solver
def solve_sudoku(board):
    def is_valid(board, row, col, num):
        # Check row and column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False
        return True
    
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            
                            if solve():
                                return True
                            
                            board[i][j] = 0  # Backtrack
                    return False
        return True
    
    solve()
    return board
```

**Key Takeaway:**
Backtracking explores all paths, undoing choices that don't lead to solution. Used for constraint satisfaction problems.

---

### 18. Dynamic Programming 🔴

**Definition:**
Breaking complex problems into overlapping subproblems and storing results to avoid recomputation.

```python
# Fibonacci with DP
def fib_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Longest Common Subsequence
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# 0/1 Knapsack
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

print(fib_dp(10))  # 55
print(lcs("ABCBDAB", "BDCAB"))  # 4
print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))  # 9
```

**Key Takeaway:**
DP stores subproblem results for O(n) or O(n²) solutions instead of exponential recursion.

---

### 19. Greedy Algorithms 🔴

**Definition:**
Makes locally optimal choice at each step, hoping to find global optimum.

```python
# Activity Selection
def activity_selection(start, finish):
    n = len(finish)
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    selected = [activities[0]]
    last_finish = activities[0][1]
    
    for i in range(1, n):
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]
    return selected

# Fractional Knapsack
def fractional_knapsack(weights, values, capacity):
    items = [(v/w, w, v) for v, w in zip(values, weights)]
    items.sort(reverse=True)
    
    total_value = 0
    for ratio, weight, value in items:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += ratio * capacity
            break
    return total_value

print(fractional_knapsack([10, 20, 30], [60, 100, 120], 50))  # 240
```

**Key Takeaway:**
Greedy makes local optimal choices. Works for problems with greedy-choice property.

---

### 20. Divide and Conquer 🔴

**Definition:**
Divide problem into smaller subproblems, solve them, and combine results.

```python
# Merge Sort (already covered)
# Quick Sort (already covered)

# Maximum Subarray (Kadane's algorithm)
def max_subarray(arr):
    max_so_far = max_ending_here = arr[0]
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Closest Pair of Points
def closest_pair_distance(points):
    def distance(p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
    
    points.sort()
    # Simplified version - O(n log n)
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            min_dist = min(min_dist, distance(points[i], points[j]))
    return min_dist

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
```

**Key Takeaway:**
Divide and conquer breaks problem into independent subproblems. Time complexity often O(n log n).

---

### 21. Two Pointers Technique 🟡

**Definition:**
Use two pointers to iterate through data structure, often from different ends.

```python
# Two Sum in Sorted Array
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Remove Duplicates
def remove_duplicates(arr):
    if not arr:
        return 0
    write_idx = 1
    for read_idx in range(1, len(arr)):
        if arr[read_idx] != arr[read_idx - 1]:
            arr[write_idx] = arr[read_idx]
            write_idx += 1
    return write_idx

print(two_sum_sorted([1, 2, 3, 4, 6], 6))  # [1, 3]
```

**Key Takeaway:**
Two pointers reduce O(n²) to O(n) for many array problems.

---

### 22. Sliding Window 🟡

**Definition:**
Maintain a window of elements and slide it through array to find optimal solution.

```python
# Maximum sum subarray of size k
def max_sum_subarray(arr, k):
    max_sum = window_sum = sum(arr[:k])
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Longest substring without repeating characters
def longest_unique_substring(s):
    char_set = set()
    left = max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

print(max_sum_subarray([1, 2, 3, 4, 5, 6], 3))  # 15
print(longest_unique_substring("abcabcbb"))  # 3
```

**Key Takeaway:**
Sliding window is efficient for contiguous subarray/substring problems, reducing complexity.

---

### 23. BFS and DFS 🟡

Already covered in Graphs section. Key applications:

```python
# BFS - Level order, shortest path
# DFS - Path finding, cycle detection, topological sort

# Connected Components
def count_islands(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs(i + di, j + dj)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```

---

### 24. Dijkstra's Algorithm 🔴

**Definition:**
Finds shortest path from source to all vertices in weighted graph with non-negative weights.

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2)],
    'E': []
}
print(dijkstra(graph, 'A'))
```

**Key Takeaway:**
Dijkstra uses priority queue for O((V + E) log V) shortest path. Fails with negative weights.

---

### 25. Bellman-Ford 🔴

**Definition:**
Finds shortest paths, handles negative weights, detects negative cycles.

```python
def bellman_ford(graph, start, n):
    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0
    
    # Relax edges n-1 times
    for _ in range(n - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
    
    # Check for negative cycles
    for u in graph:
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                return "Negative cycle detected"
    
    return distances
```

**Key Takeaway:**
Bellman-Ford: O(VE) time, handles negative weights, detects negative cycles.

---

### 26. Floyd-Warshall 🔴

**Definition:**
Finds shortest paths between all pairs of vertices using dynamic programming.

```python
def floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
    
    for u in graph:
        for v, weight in graph[u]:
            dist[u][v] = weight
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

**Key Takeaway:**
Floyd-Warshall: O(V³) time, all-pairs shortest paths, simple DP implementation.

---

### 27. Topological Sort 🟡

**Definition:**
Linear ordering of vertices in DAG where u comes before v for every edge u→v.

```python
from collections import deque

def topological_sort_bfs(graph, n):
    in_degree = [0] * n
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == n else []

def topological_sort_dfs(graph, n):
    visited = [False] * n
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
    
    return stack[::-1]
```

**Key Takeaway:**
Topological sort orders DAG vertices. Used in task scheduling, course prerequisites.

---

### 28. Minimum Spanning Tree 🔴

**Definition:**
Subset of edges connecting all vertices with minimum total weight.

**Kruskal's Algorithm:**
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    total_weight = 0
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
    
    return mst, total_weight

# Prim's Algorithm
def prim(graph, start):
    import heapq
    visited = set([start])
    edges = [(weight, start, to) for to, weight in graph[start]]
    heapq.heapify(edges)
    mst = []
    
    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            
            for next_to, next_weight in graph[to]:
                if next_to not in visited:
                    heapq.heappush(edges, (next_weight, to, next_to))
    
    return mst

edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 4)]
print(kruskal(4, edges))
```

**Key Takeaway:**
Kruskal: O(E log E), uses Union-Find. Prim: O(E log V), uses priority queue. Both find MST.

---

## ⏰ Time Complexity Cheat Sheet

### Data Structures

| Data Structure | Access | Search | Insert | Delete | Space |
|----------------|--------|--------|--------|--------|-------|
| **Array** | O(1) | O(n) | O(n) | O(n) | O(n) |
| **Linked List** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Stack** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Queue** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Hash Table** | N/A | O(1)* | O(1)* | O(1)* | O(n) |
| **Binary Search Tree** | O(log n)* | O(log n)* | O(log n)* | O(log n)* | O(n) |
| **AVL Tree** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **Heap** | O(1) | O(n) | O(log n) | O(log n) | O(n) |

*Average case; worst case can be O(n)

### Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

---

## 📊 When to Use Which Data Structure

| Use Case | Best Data Structure | Why |
|----------|-------------------|-----|
| **Fast access by index** | Array | O(1) access |
| **Frequent insertions/deletions** | Linked List | O(1) at head |
| **LIFO operations** | Stack | Function calls, undo |
| **FIFO operations** | Queue | Task scheduling, BFS |
| **Key-value pairs** | Hash Table | O(1) lookup |
| **Sorted data** | BST/AVL Tree | O(log n) operations |
| **Priority-based** | Heap | Min/max in O(1) |
| **Graph representation** | Adjacency List | Space efficient |
| **Prefix matching** | Trie | Autocomplete |

---

## 🎯 Top Problem Patterns

1. **Two Pointers**: Sorted array problems, palindromes
2. **Sliding Window**: Subarray/substring problems
3. **Fast & Slow Pointers**: Cycle detection, middle element
4. **Merge Intervals**: Overlapping intervals
5. **Cyclic Sort**: Missing numbers in range
6. **Binary Search**: Sorted array search
7. **DFS/BFS**: Tree/graph traversal
8. **Dynamic Programming**: Optimization problems
9. **Greedy**: Locally optimal choices
10. **Backtracking**: Constraint satisfaction

---

[⬆️ Back to Table of Contents](#-table-of-contents)

**Good luck with your DSA interviews! 💪🚀**
