def process_user(user):
    # Bug: Will throw AttributeError if user is None
    return user.get_id()
