def sort(array):
    return pivot_last_sort(array, 0, len(array) - 1)

def pivot_last_sort(array, first, last):
    if array is None or last - first < 2:
        return array[first:(last+1)]

    pivot = array[last]
    pos = first
    wall = first

    while pos < last:
        if array[pos] < pivot:
            temp = array[wall]
            array[wall] = array[pos]
            array[pos] = temp
            wall += 1

        pos += 1

    temp = array[wall]
    array[wall] = array[pos]
    array[pos] = temp

    return pivot_last_sort(array, first, wall-1) + pivot_last_sort(array, wall, last)

"""
after this exercise, i am going to abandon python as a language to use
for implementing sorting algorithms, as there's no reasonable way to
ensure that the algorithm is sorted in-place.
"""

