# to check whether B is a subset of A
# Python3 code to demonstrate
# to check if list is subset of other
# using all()

#initiallising lists

A = [2, 5, 7, 9]
B = [2, 5, 9]

flag = 0
if (all(x in A for x in B)):
    flag = 1

# printing result
if (flag):
    print("B is a subset of A.")
else:
    print("B is not a subset of A.")

# Python code t get difference of two lists
# Not using set()
def Diff(A, B):
	li_dif = [i for i in A + B if i not in A or i not in B]
	return li_dif

# Driver Code
A = [2, 5, 7, 9]
B = [2, 5, 9]
#list representing the set A - B
li3 = Diff(A, B)
print("A - B =",li3)

# cartesian product of A and B
from itertools import product

list1 = []

def cartesian_product(A, B):
	for i in A:
		for j in B:
			list2 = [i,j]
			list1.append(list2)
	return list1

# Driver Function
if __name__ == "__main__":
	A = [2, 5, 7, 9]
	B = [2, 5, 9]
	print(cartesian_product(A, B))

