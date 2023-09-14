class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_square_sum(num):
            # This function calculates the sum of squares of digits of a number.
            result = 0
            while num > 0:
                digit = num % 10
                result += digit * digit
                num //= 10
            return result

        # Use two pointers approach: slow and fast
        slow = n
        fast = n

        while True:
            slow = calculate_square_sum(slow)  # Move one step
            fast = calculate_square_sum(fast)  # Move two steps
            fast = calculate_square_sum(fast)

            if slow == fast:
                break  # If there's a cycle, we exit the loop

        return slow == 1  # If we reached 1, it's a happy number; otherwise, it's not

