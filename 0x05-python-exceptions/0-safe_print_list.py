#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Counter for the elements printed
    try:
        # Iterate over the elements of the list up to x or the list length
        for i in range(x):
            # Try to access the element at the current index
            try:
                element = my_list[i]
                print(element, end='')
                count += 1
            except IndexError:
                break  # Stop iteration if index is out of range
    except TypeError:
        pass  # Ignore TypeError if my_list is not iterable
    finally:
        print()  # Print a new line after the elements

    return count
