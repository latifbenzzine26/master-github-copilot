import sys


def main() -> None:
    """Read two integers from standard input and print their sum."""
    first = int(sys.stdin.readline())
    second = int(sys.stdin.readline())
    print(first + second)


if __name__ == "__main__":
    main()
