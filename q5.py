#get user input

def user_lists(list1, list2):
    # numbs = input("Enter a list of numbers separated by a space ")
    # list1  = numbs.split()
    # print(list1)
    # input_string = input("Enter another list element separated by a space ")
    # list2 = input_string.split()
    # print(list2)

   #x is a factor of y, and y is divisible by x.

    for x in list1:
        for y in list2:
            if x % y == 0:
                print(True)
            else:
                print(False)

x = [4, 8, 10]
y = [2, 4, 6]

user_lists(x, y)





