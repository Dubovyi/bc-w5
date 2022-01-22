if __name__ == '__main__':
    data = input().strip().split()
    dividend, divisor = map(int, data)

    if divisor < 0:
        divisor *= -1

    multiple = dividend - dividend % divisor

    if multiple < dividend:
        multiple += divisor

    print(f'multiple: {multiple}')