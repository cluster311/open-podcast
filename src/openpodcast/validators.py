def validate_string(value, max_length=None):
    if type(value) != str:
        return False, f"'{value}' is not string. '{type(value)}' found"
    if max_length is not None and len(value) > max_length:
        return False, f"'{value}' is too long. '{len(value)} > {max_length}'"
    return True, None


def validate_int(value, min_value=0, max_value=None):
    if type(value) != int:
        return False, f"'{value}' is not integer. '{type(value)}' found"
    if min_value is not None and value < min_value:
        return False, f"'{value}' is less than the minimum allowed value '{min_value}'"
    if max_value is not None and value > max_value:
        return False, f"'{value}' is greater than the maximum allowed value '{max_value}'"
    return True, None
