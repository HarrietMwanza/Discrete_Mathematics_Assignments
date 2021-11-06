def truth_values(a, b):
    for i in a:
        for j in b:
            cartesian_pro = [i, j]
            print(cartesian_pro)

    # if list1 == B:
    #     print(True, "Set B is a subset of set A")
    # else:
    #     print(False, "Set B is not a subset of Set A")


truth_values([1, 2, 3], [5, 1, 3])


def sets_functions(a, b):
    list_A = set(a)
    list_B = set(b)
    # Finding if B is a subset of A
    x = list_B.issubset(list_A)
    print(x)

    # Finding the difference between A and B
    y = list_A.difference(list_B)
    print(y)
    # Returning the intersection of A and B
    # z = A.intersection(B)

    # Returning the truth value of B subset A
    # print(x)
    # # Printing the difference between A and B
    # print(y)
    # # Printing the intersection of A and B
    # print(z)


B = {"a", "b", "c"}
A = {"f", "e", "d", "c", "b", "a"}
sets_functions(A, B)
