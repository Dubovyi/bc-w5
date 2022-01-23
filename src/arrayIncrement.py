def array_increment(arr):
    tmpArr = []

    for i in arr:
        tmpArr.append(i + 1)

    return tmpArr


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]

    print('array before increment', array)
    array = array_increment(array)
    print('array after increment', array)
