def check_positive(num):
    # Bug: 0 is not positive, logic might be flawed if expecting > 0 strictly
    if num >= 0:
        return True
    return False
