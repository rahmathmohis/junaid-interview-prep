"""
Problem #2: Fibonacci Series up to Nth Term
Difficulty: 🟢 Easy
Topics: Recursion, Dynamic Programming, Math

Time Complexity:
- Brute Force (Recursive): O(2^n) - exponential
- Efficient (Iterative): O(n) - linear
- Optimal (Matrix Exponentiation): O(log n)

Space Complexity:
- Brute Force: O(n) - call stack
- Efficient: O(n) - for result list, O(1) working space
"""


def fibonacci_brute(n: int) -> list:
    """
    Brute Force Approach: Recursive calculation for each term
    
    Time Complexity: O(2^n) - exponential due to repeated calculations
    Space Complexity: O(n) - recursion call stack
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    series = []
    
    def fib_rec(k: int) -> int:
        """Calculate kth Fibonacci number recursively"""
        if k <= 1:
            return k
        return fib_rec(k - 1) + fib_rec(k - 2)
    
    for i in range(n):
        series.append(fib_rec(i))
    
    return series


def fibonacci_efficient(n: int) -> list:
    """
    Efficient Approach: Iterative calculation
    
    Time Complexity: O(n) - single pass
    Space Complexity: O(n) - for result list, O(1) working space
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    series = [0, 1]
    
    for i in range(2, n):
        next_fib = series[-1] + series[-2]
        series.append(next_fib)
    
    return series


def fibonacci_nth_term(n: int) -> int:
    """
    Get only the nth Fibonacci term (0-indexed)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


def fibonacci_memoized(n: int, memo: dict = None) -> list:
    """
    Memoized Recursive Approach (Top-Down DP)
    
    Time Complexity: O(n) - each value calculated once
    Space Complexity: O(n) - memo dictionary + call stack
    """
    if memo is None:
        memo = {}
    
    if n <= 0:
        return []
    
    def fib_memo(k: int) -> int:
        if k in memo:
            return memo[k]
        if k <= 1:
            memo[k] = k
        else:
            memo[k] = fib_memo(k - 1) + fib_memo(k - 2)
        return memo[k]
    
    series = []
    for i in range(n):
        series.append(fib_memo(i))
    
    return series


def run_tests():
    """Test cases to validate all solutions"""
    print("🧪 Running Test Cases for Fibonacci Series...\n")
    
    test_cases = [
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
        (0, []),
        (15, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]),
    ]
    
    all_passed = True
    
    for i, (input_val, expected) in enumerate(test_cases, 1):
        efficient_result = fibonacci_efficient(input_val)
        memoized_result = fibonacci_memoized(input_val)
        
        efficient_pass = efficient_result == expected
        memoized_pass = memoized_result == expected
        
        if efficient_pass and memoized_pass:
            print(f"✅ Test {i} passed: fib({input_val}) = {expected}")
        else:
            print(f"❌ Test {i} failed:")
            print(f"   Input: {input_val}, Expected: {expected}")
            if not efficient_pass:
                print(f"   Efficient got: {efficient_result}")
            if not memoized_pass:
                print(f"   Memoized got: {memoized_result}")
            all_passed = False
    
    # Test individual term calculation
    print("\n🧪 Testing nth term calculation...")
    term_tests = [
        (0, 0),
        (1, 1),
        (5, 5),
        (10, 55),
        (15, 610),
    ]
    
    for n, expected in term_tests:
        result = fibonacci_nth_term(n)
        if result == expected:
            print(f"✅ Term {n}: {result}")
        else:
            print(f"❌ Term {n}: got {result}, expected {expected}")
            all_passed = False
    
    return all_passed


if __name__ == "__main__":
    print("=" * 60)
    print("Problem #2: Fibonacci Series up to Nth Term")
    print("=" * 60)
    
    # Example usage
    n = 10
    print(f"\n📝 Example (n = {n}):")
    print(f"   Brute Force:  {fibonacci_brute(n)}")
    print(f"   Efficient:    {fibonacci_efficient(n)}")
    print(f"   Memoized:     {fibonacci_memoized(n)}")
    print(f"   10th term:    {fibonacci_nth_term(10)}")
    
    print("\n" + "=" * 60)
    success = run_tests()
    print("=" * 60)
    
    if success:
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Some tests failed!")
        exit(1)
