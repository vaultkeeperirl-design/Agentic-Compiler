def fetch_item(data_dict, key):
    # Bug: Will throw KeyError if key does not exist
    return data_dict[key]
