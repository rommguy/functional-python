from list import Nil, cons, head, tail
from functions import flip, compose
from pair import pair, fst, snd

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
    return lambda lst: Nil if nil(lst) or n == 0 else cons(head(lst))(take(n - 1)(tail(lst)))


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
    return lambda lst2: lst2 if nil(lst1) else cons(head(lst1))(concat(tail(lst1))(lst2))


# 10.
def reverse(lst):
    return Nil if nil(lst) else cons(last(lst))(reverse(init(lst)))


# 11.
def filter_f(p):
    return (
        lambda list_f: Nil
        if nil(list_f)
        else filter_f(p)(tail(list_f))
        if not p(head(list_f))
        else cons(head(list_f))(filter_f(p)(tail(list_f)))
    )


# 12.
def map_f(f):
    return lambda list_f: Nil if nil(list_f) else cons(f(head(list_f)))(map_f(f)(tail(list_f)))


# 13.
def foldl(f):
    return (
        lambda accm: lambda list_f: accm
        if nil(list_f)
        else foldl(f)(f(accm)(head(list_f)))(tail(list_f))
    )


# 14.
def foldr(f):
    return (
        lambda accm: lambda list_f: accm
        if nil(list_f)
        else f(head(list_f))(foldr(f)(accm)(tail(list_f)))
    )


# 15.
def copy(list_f):
    return foldl(flip(cons))(Nil)(reverse(list_f))


# 16.
copy2 = foldr(cons)(Nil)


# 17.
def func_map2(f):
    return foldr(compose(cons)(f))(Nil)


# 18.
reverse2 = foldl(flip(cons))(Nil)


# 19.
def zip_f(a_lst_f):
    return (
        lambda b_lst_f: Nil
        if nil(a_lst_f) or nil(b_lst_f)
        else cons(pair(head(a_lst_f))(head(b_lst_f)))(zip_f(tail(a_lst_f))(tail(b_lst_f)))
    )


# 20.
def unzip_func(list_pairs):
    if nil(list_pairs):
        return pair(Nil)(Nil)
    else:
        tail_unzipped = unzip_func(tail(list_pairs))
        head_pair = head(list_pairs)
        return pair(cons(fst(head_pair))(fst(tail_unzipped)))(
            cons(snd(head_pair))(snd(tail_unzipped))
        )
