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
def length(lst):
    return 0 if nil(lst) else 1 + length(tail(lst))


# 6.
def take(n):
    return (
        lambda lst: Nil
        if nil(lst) or n == 0
        else cons(head(lst))(take(n - 1)(tail(lst)))
    )


# 7.
def drop(n):
    return lambda lst: lst if nil(lst) or n == 0 else drop(n - 1)(tail(lst))


# 8.
def eq(lst1):
    return (
        lambda lst2: True
        if nil(lst1)
        and nil(lst2)
        or not nil(lst1)
        and not nil(lst2)
        and head(lst1) == head(lst2)
        and eq(tail(lst1))(tail(lst2))
        else False
    )


# 9.
def concat(lst1):
    return (
        lambda lst2: lst2 if nil(lst1) else cons(head(lst1))(concat(tail(lst1))(lst2))
    )


# 10.
def reverse(lst):
    return Nil if nil(lst) else cons(last(lst))(reverse(init(lst)))
