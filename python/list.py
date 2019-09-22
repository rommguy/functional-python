from functools import reduce

Nil = "NIL"


def cons(list_head):
    return lambda list_tail: {"_head": list_head, "_tail": list_tail}


def head(fc_list):
    if fc_list == Nil:
        raise Exception
    else:
        return fc_list["_head"]


def tail(fc_list):
    if fc_list == Nil:
        raise Exception
    else:
        return fc_list["_tail"]


def Lst(*elements):
    new_elements = [*elements]
    new_elements.reverse()
    return reduce(lambda accu, a: cons(a)(accu), new_elements, Nil)
