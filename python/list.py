from functools import reduce

Nil = "NIL"


def cons(list_head):
    def create_list(list_tail):
        list_f = ListF()
        list_f._head = list_head
        list_f._tail = list_tail
        return list_f

    return create_list


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


class ListF:
    def __init__(self, *elements):
        new_elements = [*elements]
        if len(new_elements) > 0:
            new_elements.reverse()
            res = reduce(lambda accu, a: cons(a)(accu), new_elements, Nil)
            self._tail = tail(res)
            self._head = head(res)

    def __eq__(self, other):
        if not isinstance(other, ListF):
            return False
        head_same = head(self) == head(other)
        if tail(self) != Nil and tail(other) != Nil:
            return head_same and tail(self) == tail(other)
        return tail(self) == Nil and tail(other) == Nil

    def __repr__(self):
        return str(head(self)) + "," + str(tail(self))


def ListF2(*elements):
    new_elements = [*elements]
    new_elements.reverse()
    return reduce(lambda accu, a: cons(a)(accu), new_elements, Nil)
