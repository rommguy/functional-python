from functools import reduce

Nil = "NIL"


def cons(head):
    return lambda tail: {"_head": head, "_tail": tail}


def head(fc_list):
    if fc_list == Nil:
        raise Exception
    else:
        return fc_list._head


def tail(fc_list):
    if fc_list == Nil:
        raise Exception
    else:
        return fc_list._tail


def Lst(*elements):
    new_elements = [*elements]
    reduce(lambda accu, a: cons(a)(accu), new_elements.reverse(), Nil)
