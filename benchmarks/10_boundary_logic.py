def is_valid_password(pwd):
    # Bug: Logic incorrectly rejects passwords > 8, should accept them
    if len(pwd) < 8 or len(pwd) > 8:
        return False
    return True
