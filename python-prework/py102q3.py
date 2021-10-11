def max_num_in_list(a_list):
    """Return max number of a given list."""
    a_list.sort()
    print(a_list.pop())

max_num_in_list(a_list=[1,5,100,110,15,1000,12,52,88,500])