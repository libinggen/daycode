def getMin(s: str) -> int:
    left_needed = 0
    right_needed = 0

    for char in s:
        if char == '(':
            left_needed += 1
        elif char == ')':
            if left_needed > 0:
                left_needed -= 1
            else:
                right_needed += 1

    return left_needed + right_needed