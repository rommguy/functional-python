from list import Nil, cons, head, tail


# 1.
def nil(lst):
    return lst == Nil


# 2.
def init(lst):
    return (lambda t: Nil if nil(t) else cons(head(lst))(init(t)))(tail(lst))


# 3.
def last(lst):
    return (lambda t: head(lst) if nil(t) else last(t))(tail(lst))


# 4.
def elem(e):
    def inner(lst):
        if nil(lst):
            return False
        elif head(lst) == e:
            return True
        else:
            return elem(e)(tail(lst))

    return inner


# 5.
