# -*- coding: utf-8 -*-
def fact(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    print(result)

# Some comment
def main():
    fact(8)


if __name__ == '__main__':
    main()
