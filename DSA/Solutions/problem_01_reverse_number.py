"""
Problem #1: Reverse a Number
Difficulty: 🟢 Easy
Topics: Math, Number Theory

Time Complexity:
- Brute Force: O(d) where d = number of digits
- Efficient: O(d) where d = number of digits

Space Complexity:
- Brute Force: O(d) for string conversion
- Efficient: O(1) constant space
"""


def reverse_number_brute(n: int) -> int:
    """
    Brute Force Approach: Convert to string, reverse, convert back
    
    Time Complexity: O(d) where d = number of digits
    Space Complexity: O(d) for string storage
    """
    sign = -1 if n < 0 else 1
    reversed_str = str(abs(n))[::-1]
    return sign * int(reversed_str)


def reverse_number_efficient(n: int) -> int:
    """
    Efficient Approach: Mathematical approach using modulo and division
    
    Time Complexity: O(d) where d = number of digits
    Space Complexity: O(1) - only using constant extra space
    """
    sign = -1 if n < 0 else 1
    n = abs(n)
    result = 0
    
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    
    return sign * result


def reverse_number_with_overflow_check(n: int) -> int:
    """
    Advanced: With 32-bit integer overflow check
    
    Time Complexity: O(d)
    Space Complexity: O(1)
    
    Returns 0 if overflow occurs (for 32-bit signed integer range)
    """
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    sign = -1 if n < 0 else 1
    n = abs(n)
    result = 0
    
    while n > 0:
        digit = n % 10
        # Check for overflow before it happens
        if result > (INT_MAX - digit) // 10:
            return 0
        result = result * 10 + digit
        n //= 10
    
    return sign * result


def run_tests():
    """Test cases to validate all solutions"""
    print("🧪 Running Test Cases for Reverse Number...\n")
    
    test_cases = [
        (12345, 54321),
        (-12345, -54321),
        (100, 1),
        (0, 0),
        (7, 7),
        (98765, 56789),
        (1200, 21),
        (-500, -5),
    ]
    
    all_passed = True
    
    for i, (input_val, expected) in enumerate(test_cases, 1):
        brute_result = reverse_number_brute(input_val)
        efficient_result = reverse_number_efficient(input_val)
        
        brute_pass = brute_result == expected
        efficient_pass = efficient_result == expected
        
        if brute_pass and efficient_pass:
            print(f"✅ Test {i} passed: reverse({input_val}) = {expected}")
        else:
            print(f"❌ Test {i} failed:")
            print(f"   Input: {input_val}, Expected: {expected}")
            if not brute_pass:
                print(f"   Brute Force got: {brute_result}")
            if not efficient_pass:
                print(f"   Efficient got: {efficient_result}")
            all_passed = False
    
    # Test overflow case
    print("\n🧪 Testing overflow handling...")
    overflow_test = 2**31  # This should cause overflow
    overflow_result = reverse_number_with_overflow_check(overflow_test)
    if overflow_result == 0:
        print(f"✅ Overflow test passed: reverse({overflow_test}) = 0 (correctly detected)")
    else:
        print(f"❌ Overflow test failed: got {overflow_result}, expected 0")
        all_passed = False
    
    return all_passed


if __name__ == "__main__":
    print("=" * 60)
    print("Problem #1: Reverse a Number")
    print("=" * 60)
    
    # Example usage
    num = 12345
    print(f"\n📝 Example:")
    print(f"   Input: {num}")
    print(f"   Brute Force:  {reverse_number_brute(num)}")
    print(f"   Efficient:    {reverse_number_efficient(num)}")
    print(f"   With Overflow Check: {reverse_number_with_overflow_check(num)}")
    
    print("\n" + "=" * 60)
    success = run_tests()
    print("=" * 60)
    
    if success:
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Some tests failed!")
        exit(1)
