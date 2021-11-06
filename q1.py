# we are checking if two lists have common elements in them.
# if true print the list
# if false print the list converted to a set

def common_elements(list_1):

    a_set = set(list_1)
    # b_set = set(list_2)
    if len(list_1) == len(a_set):
        return True
    else:

        return "False, {}".format(a_set)

#here is our given lists

list_one = [1, 2, 5, 7, 58, 7]
list_two = [87, 58, 0, 3, 1]
print("Are elements common between list_one and list_two?")
print(common_elements(list_one))
list_three = [0, 5, 7, 89, 34, 4]
list_four = [45, 78, 90]
print("Are elements common between list_three and list_four?")
print(common_elements(list_three))
