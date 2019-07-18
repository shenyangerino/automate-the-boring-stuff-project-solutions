# Write a function that takes a list value as an argument and returns a string with all the items separated
# by a comma and a space, with and inserted before the last item.
# For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
# But your function should be able to work with any list value passed to it.

def comma(list):
    list = ", ".join(map(str, list))    # To get the newly joined 'list', need to assign formatted 'list' as 'list'
                                        # map(str, list) is used to be sure that non-string items can also be joined
                                        # by first, converting all items to string
    return list

spam = ['apples', 10, 'tofu', 'cats']

print(comma(spam))
