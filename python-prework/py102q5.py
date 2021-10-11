# I had trouble with this one and couldnt figure out how to write this-
# code myself, i reached out to a friend for help.
def is_consecutive(a_list):

    y = (a_list[0])
    for item in (a_list):
        if(item != y):
            return False
        else:
            y += 1
    return True
    

print(is_consecutive([1,2,3,4,5,7]))
print(is_consecutive([1,2,3,4,5]))
print(is_consecutive([1,2,3,4,5]))
print(is_consecutive([1,2,3,4,5,6,7,8]))