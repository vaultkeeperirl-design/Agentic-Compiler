def calculate_sum(numbers):
    # Bug: Starts index at 1, missing the first element
    total = 0
    for i in range(1, len(numbers)):
        total += numbers[i]
    return total
