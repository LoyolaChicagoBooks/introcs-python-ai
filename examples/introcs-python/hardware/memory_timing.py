import sys
import time


def main() -> None:
    # A list of one million integers lives in RAM.
    numbers = list(range(1_000_000))
    print(f"RAM used by list: {sys.getsizeof(numbers):,} bytes")

    # Summing values already in RAM is fast.
    start = time.perf_counter()
    total = sum(numbers)
    ram_time = time.perf_counter() - start

    # Writing those values to a file and reading them back is much slower.
    with open("numbers.txt", "w") as f:
        f.write("\n".join(str(n) for n in numbers))

    start = time.perf_counter()
    with open("numbers.txt") as f:
        total = sum(int(line) for line in f)
    disk_time = time.perf_counter() - start

    print(f"RAM  time: {ram_time:.4f} s")
    print(f"Disk time: {disk_time:.4f} s")


if __name__ == "__main__":
    main()
