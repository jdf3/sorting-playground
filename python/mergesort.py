def sort(array):
    if array is None or len(array) < 2:
        return array
    
    s = int(len(array)/2)

    first = sort(array[:s])
    second = sort(array[s:])

    fp = 0
    sp = 0
    result = []
    
    while fp < len(first) or sp < len(second):
        if fp >= len(first):
            result.extend(second[sp:])
            sp = len(second)
        elif sp >= len(second):
            result.extend(first[fp:])
            fp = len(first)
        elif first[fp] < second[sp]:
            result.append(first[fp])
            fp += 1
        else:
            result.append(second[sp])
            sp += 1

    return result
