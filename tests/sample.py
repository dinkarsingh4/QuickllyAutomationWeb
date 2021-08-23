def reverse(lst):
    new_list = []
    for i in range(len(lst)):
        new_list.insert(i, lst[-1])
        lst.pop(-1)
    print(new_list)


my_list = [1, 2, 3, 4, 5]
reverse(my_list)
