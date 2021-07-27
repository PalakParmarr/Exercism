def append(list1, list2):
    return list1+list2


def concat(lists):
    result = []
    for l in lists:
        result = append(result, l)
    return result


def filter(function, list):
    l = []
    for item in list:
        if function(item):
            l.append(item)
    return l


def length(list):
    return len(list)


def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result

def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function, list, initial):
    result = initial
    for item in reverse(list):
        result = function(item, result)
    return result


def reverse(list):
    return list[::-1]


