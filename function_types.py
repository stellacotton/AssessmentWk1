
def largest(l):
    candidate = l[0]
    for item in l:
        if item > candidate:
            candidate = item

    return candidate


def sum(l):
    total = 0
    for item in l:
        total = total + item



def reduce(l, start, fn):
    candidate = start
    for item in l:
        candidate = fn(item, candidate)


def add(x, y):
    return x + y

def max(x, y):
    if x > y:
        return x
    else:
        return y

def sum_r(l):
    return reduce(l, 0, add)


def largest_r(l):
    return reduce(l, l[0], max)




def filter(l, fn):
    new_list = []
    for item in l:
        if fn(item) == True:
            new_list.append(item)


def even_num(x):
    if x % 2 == 0:
        True

def even_f(l):
    return filter(l, even_num)


my_list = [1,2,3,4]


print filter(my_list, even_f)