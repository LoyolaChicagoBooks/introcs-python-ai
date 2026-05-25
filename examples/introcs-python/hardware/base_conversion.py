def to_base(n, base):
    if n == 0:
        return "0"
    chars = "0123456789ABCDEF"
    negative = n < 0
    n = abs(n)
    result = []
    while n > 0:
        digit = n % base
        result.append(chars[digit] if base <= 16 else str(digit))
        n //= base
    result.reverse()
    digits_str = "".join(result) if base <= 16 else ":".join(result)
    return ("-" + digits_str) if negative else digits_str


def main() -> None:
    # Standard bases
    print(to_base(42, 2))     # binary
    print(to_base(42, 8))     # octal
    print(to_base(42, 16))    # hexadecimal
    print(to_base(-42, 2))    # negative number
    print(to_base(255, 16))   # one full byte in hex

    # Base 7
    print(to_base(42, 7))     # 6*7 + 0
    print(to_base(100, 7))    # 2*49 + 0*7 + 2
    print(to_base(-42, 7))    # negative in base 7

    # Base 60 - sexagesimal (Babylonian)
    print(to_base(42, 60))    # less than 60: single group
    print(to_base(90, 60))    # 1*60 + 30, like 1 min 30 sec
    print(to_base(3600, 60))  # 1*3600 + 0 + 0, like 1 hour
    print(to_base(3661, 60))  # 1*3600 + 1*60 + 1, like 1:01:01


if __name__ == "__main__":
    main()
