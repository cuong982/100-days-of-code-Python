"""
b.append(4)

print(b) # [1, 2, 3, 4]
print(a) # [1, 2, 3, 4]
"""


def test_copy_list_with_side_effect():
    a = [1, 2, 3]
    b = a
    b.append(4)

    print(b)  # [1, 2, 3, 4]
    print(a)  # [1, 2, 3, 4]


def test_copy_without_side_effect():
    a = [1, 2, 3]
    b = a[:]
    print(b)

    b = a.copy()
    print(b)

    import copy
    b = copy.copy(a)
    print(b)


def shallow_copying():
    a = [[1, 2], [3, 4]]

    b = a[:]
    # or:
    # b = a.copy()
    # b = list(a)
    # b = copy.copy(a)

    b[0].append(99)
    print(b)  # [[1, 2, 99], [3, 4]]
    print(a)  # [[1, 2, 99], [3, 4]]


def deep_copying():
    import copy

    a = [[1, 2], [3, 4]]

    b = copy.deepcopy(a)

    b[0].append(99)

    print(b)  # [[1, 2, 99], [3, 4]]
    print(a)  # [[1, 2], [3, 4]]


if __name__ == '__main__':
    # print(timeit.timeit(lambda: "-".join(map(str, range(100))), number=1000))
    print('______START______')
    test_copy_list_with_side_effect()
    test_copy_without_side_effect()
    shallow_copying()
    deep_copying()
    print('_______END_______')
