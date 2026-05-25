# start: safe_divide
def safe_divide(a: float, b: float) -> float:
    """Return a / b, raising ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    try:
        result = safe_divide(10, 0)
    except ValueError as e:
        print(e)
# end: safe_divide

    print(safe_divide(10, 4))
