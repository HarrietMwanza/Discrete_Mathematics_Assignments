def checkIfSet(R):
    count = 0
    for item in R:
        for subset in R:
            if item == subset:
                count += 1
        if count == 2:
            return 'R is not a set'
        else:
            count = 0

    return 'R is a set'

def contains_all(A, R):
    for item in R:
        if item[0] not in A or item[1] not in A:
            return "R is not a subset of A"

    return 'R is a subset of A'

def checkIfRelation(A, R):
    for item in R:
        if item[0] not in A or item[1] not in A:
            return "R is not a relation"

    return 'R is a relation on A'

def reflexive(R, A):
    """Returns True if a relation R on set A is reflexive, False otherwise."""
    for a in A:
        templist = [a, a]
        if templist not in R:
            print('R is not reflexive : ' + str(a))

def symmetric(R, A):
    for a, b in R:
        templist = [a, b]
        templist2 = [b, a]
        if templist2 not in R:
            return 'R is not symmetric : ' + str(templist)

def is_transitive(f, domain):
    for i in domain:
        for j in domain:
            for k in domain:
                subset_a = [i, j]
                subset_b = [j, k]
                subset_c = [i, k]
                if subset_a in f and subset_b in f and subset_c not in f:
                    return "R is not transitive : " + str(subset_a)

    return "transitive"

if __name__ == "__main__":

    A = [1, 3, 4, 5]
    R = [[1, 1], [1, 5], [5, 1], [5, 5], [3, 4], [4, 1], [4, 4]]

    print(checkIfSet(R))
    print(contains_all(A, R))
    print(checkIfRelation(A, R))
    reflexive(R, A)
    print(symmetric(R, A))
    print(is_transitive(R, A))
def contains_all(A, R):
    for item in R:
        if item[0] not in A or item[1] not in A:
            return "R is not a subset of A because the following element is in R but not in A : " + str(item[0])

    return 'R is a subset of A'

def checkIfRelation(A, R):
    for item in R:
        if item[0] not in A or item[1] not in A:
            return "R is not a relation on A"

    return 'R is a relation on A'

if __name__ == "__main__":

    A = [1, 2, 4, 5]
    R = [[1, 1], [1, 5], [5, 1], [5, 5], [3, 4], [4, 1], [4, 4]]

    print(checkIfSet(R))
    print(contains_all(A, R))
    print(checkIfRelation(A, R))


