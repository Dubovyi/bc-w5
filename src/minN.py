if __name__ == '__main__':
    count = int(input())
    array = []
    i = 0

    while i < count:
        tmp = int(input())
        array.append(tmp)
        i += 1

    print(min(array))
