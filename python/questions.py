from python.list import cons, head, tail, Nil, Lst
from python.test import TestApi
from python.functions import flip, compose, identity, constant
from python.pair import pair, fst, snd


def main_program():
    """
  In this test, a basic implementation of a linked list data structure is given.

  In each question below, you should implement a function that passes all the
  given tests according to the instructions.

  When implementing a function, follow these rules:

  - Don't mutate variables
  - Your functions should accept only one argument

  The last rule means that you should do this:

  add = lambda a: lambda b: a + b
  result = add (1) (2)

  instead of this:

  add = lambda a, b: a + b
  result = add(1, 2)

  The implementation of list in this test has the following building blocks:

  - Nil -
  'Nil' is the empty list. This is how you use 'Nil':

  myEmptyList = Nil

  - cons -
  Type: cons :: a -> [a] -> [a]

  'cons' is the list constructor. It is a function that takes a 'head' and 'tail'
  and returns a new list. The 'head' is any value and the 'tail' is
  a list. This is how you use 'cons':

  my_singleton_list = cons (2) (Nil) // This will return the list: [2]
  my_two_element_list = cons (1) (my_singleton_list) // This will return the list: [1, 2]
  my_three_element_list = cons (1) (cons (2) (cons (3) (Nil))) // This will return the list: [1, 2, 3]

  - head -
  Type: head :: [a] -> a

  'head' is a function that takes a non-empty list and returns its head. The head
  is the first element in the list. This is how you use 'head':

  my_head = head (my_three_element_list) // This will return 1
  no_head = head (Nil) // This will throw an error since the list is empty

  - tail -
  Type: tail :: [a] -> [a]

  'tail' is a function that takes a non-empty list and returns its tail. The tail
  is a list with all elements except for the first one. This is how you use 'tail':

  myTail = tail (my_three_element_list) // This will return the list: [2, 3]
  noTail = tail (Nil) // This will throw an error since the list is empty

  As you can see, the following will hold for any non-empty list l:

  cons (head (l)) (tail (l)) === l

  --------------------------------------------------------------------------------

  Each question has a short description followed by some tests.
  To start implementing the question functions, open the list.html file in chrome.
  Go over the questions one by one and implement the required function.
  When you are done with a question, refresh chrome and make sure the tests pass.
  The html page will present the test results in green for success and red for
  failure.

  In your answers you may use the following functions:

  - flip -
  Type: flip :: (a -> b -> c) -> (b -> a -> c)

  'flip' is a higher order function that given a binary function returns a
  binary function which invokes the given function with the arguments flipped

  flip = f => a => b => f (b) (a)

  For example:

  div = a => b => a / b
  div (2) (5) // This will result in 0.4
  flip (div) (2) (5) // This will result in 2.5

  - compose -
  Type: compose :: (b -> c) -> (a -> b) -> (a -> c)
  'compose' does function composition

  compose = f => g => x => f (g (x))

  For example:

  square = x => x ** 2
  square (3) // This will result in 9
  compose (square) (square) (3) // This will result in 81

  - identity -
  Type: identity :: a -> a

  'identity' is identity function

  identity = x => x

  For example:

  identity (42) // This will result in 42

  - constant =
  Type: constant :: a -> b -> a

  'constant' is the constant function

  const constant = x => _ => x

  For examples:

  constant (1) (1) // This will result in 1
  constant (1) (2) // This will result in 1
  constant (1) ('hello') // This will result in 1
  constant (1) () // This will result in 1


  Good luck!


  */
  """

    test_api = TestApi()
    expect = test_api.expect
    test = test_api.test

    """
    ////////////////////////////////////////////////////////////////////////////////
    // 1.
    // Implement the 'nil' function which returns true if the list is Nil and false otherwise
    //
    // Type: nil :: [a] -> boolean
    // Signature: nil = list => ...
    """

    def nil(lst):
        return lst == Nil

    def testing_nil():
        expect("1. nil on empty list", nil(Nil), True)
        expect("1. nil on empty list", nil(Lst(1, 2, 3)), False)

    test(nil, testing_nil)

    """
    ////////////////////////////////////////////////////////////////////////////////
    2.
     Implement the 'init' function which returns all the elements of a
     list except the last one. The list must be non-empty
    
     Type: init :: [a] -> [a]
     Signature: init = lst => ...
    """

    def init(lst):
        return (lambda t: Nil if nil(t) else cons(head(lst))(init(t)))(tail(lst))

    def testing_init():
        expect(
            "2. The first element in the init of a list", head(init(Lst(1, 2, 3))), 1
        )
        expect(
            "2. The second element in the init of a list",
            head(tail(init(Lst(1, 2, 3)))),
            2,
        )
        expect("2. The init length should be 2", tail(tail(init(Lst(1, 2, 3)))), Nil)

    test(init, testing_init)

    """
    ////////////////////////////////////////////////////////////////////////////////
     3.
     Implement the 'last' function which returns the last element in the list
    
     Type: last :: [a] -> a
     Signature: last = list => ...
    """

    def last(lst):
        return (lambda t: head(lst) if nil(t) else last(t))(tail(lst))

    def testing_last():
        expect("3. tail of a list", last(Lst(1, 2, 3)), 3)
        expect("3. tail of a singleton list", last(Lst(1)), 1)

    test(last, testing_last)

    """
    ////////////////////////////////////////////////////////////////////////////////
     4.
     Implement the 'elem' function which return true if the element occurs in the
     list and false otherwise
    
     Type: elem :: a -> [a] -> boolean
     Signature: elem = e => list => ...
    """

    def elem(e):
        def inner(lst):
            if nil(lst):
                return False
            elif head(lst) == e:
                return True
            else:
                return elem(e)(tail(lst))

        return inner

    def testing_elem():
        expect(" 4. Element should not be found in an empty list", elem(1)(Nil), False)
        expect(" 4. Existing element is first", elem(1)(Lst(1, 2, 3)), True)
        expect(" 4. Existing element is last", elem(1)(Lst(3, 2, 1)), True)
        expect(" 4. Existing element in a singleton list", elem(1)(Lst(1)), True)
        expect(" 4. Non-existing element", elem(4)(Lst(1, 2, 3)), False)

    test(elem, testing_elem)

    """
    ////////////////////////////////////////////////////////////////////////////////
    5.
    Implement the 'length' function which returns the number of elements in the list
    
    Type: length :: [a] -> number
    Signature: length = list => ...
    """

    def length(lst):
        return 0 if nil(lst) else 1 + length(tail(lst))

    def testing_length():
        expect(" 5. The length of an empty list should be 0", length(Nil), 0)
        expect(" 5. The length of a singleton list should be 1", length(Lst(1)), 1)
        expect(
            " 5. The length of a list with 3 elements should be 3",
            length(Lst(1, 2, 3)),
            3,
        )

    test(length, testing_length)

    """
    ////////////////////////////////////////////////////////////////////////////////
    6.
    Implement the 'take' function which return the prefix of list of length n.
    If n > length(list), return list
    
    Type: take :: number -> [a] -> [a]
    Signature: take = n => list => ...
    """

    def take(n):
        return (
            lambda lst: Nil
            if nil(lst) or n == 0
            else cons(head(lst))(take(n - 1)(tail(lst)))
        )

    def testing_take():
        expect(" 6. Taking 0 from Nil", take(0)(Nil), Nil)
        expect(" 6. Taking 3 from Nil", take(3)(Nil), Nil)
        expect(" 6. Taking 0 from a list of 3", take(0)(Lst(1, 2, 3)), Nil)
        expect(" 6. Taking 1 from a list of 3", take(1)(Lst(1, 2, 3)), Lst(1))
        expect(" 6. Taking 2 from a list of 3", take(2)(Lst(1, 2, 3)), Lst(1, 2))
        expect(" 6. Taking 3 from a list of 3", take(3)(Lst(1, 2, 3)), Lst(1, 2, 3))
        expect(" 6. Taking 4 from a list of 3", take(4)(Lst(1, 2, 3)), Lst(1, 2, 3))

    test(take, testing_take)

    """
    ////////////////////////////////////////////////////////////////////////////////
    7.
    Implement the 'drop' function which returns the suffix of list after the first n elements.
    If n > length(list), return Nil
    
    Type: drop :: number -> [a] -> [a]
    Signature: drop = n => list => ...
    """

    def drop(n):
        return lambda lst: lst if nil(lst) or n == 0 else drop(n - 1)(tail(lst))

    def testing_drop():
        expect(" 7. Dropping 0 from Nil", drop(0)(Nil), Nil)
        expect(" 7. Dropping 3 from Nil", drop(3)(Nil), Nil)
        expect(" 7. Dropping 0 from a list of 3", drop(0)(Lst(1, 2, 3)), Lst(1, 2, 3))
        expect(" 7. Dropping 1 from a list of 3", drop(1)(Lst(1, 2, 3)), Lst(2, 3))
        expect(" 7. Dropping 2 from a list of 3", drop(2)(Lst(1, 2, 3)), Lst(3))
        expect(" 7. Dropping 3 from a list of 3", drop(3)(Lst(1, 2, 3)), Nil)
        expect(" 7. Dropping 4 from a list of 3", drop(4)(Lst(1, 2, 3)), Nil)

    test(drop, testing_drop)

    """
    // 8.
    Implement the 'eq' function which returns 'true' if the lists are equal
    and 'false' otherwise
    
    Type: eq :: [a] -> [a] -> boolean
    Signature: eq = as => bs => ...
    """

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

    def testing_eq():
        expect(" 8. Empty list equality", eq(Nil)(Nil), True)
        expect(" 8. Non-empty list equality", eq(Lst(1, 2, 3))(Lst(1, 2, 3)), True)
        expect(" 8. Long and short lists", eq(Lst(1, 2, 3))(Lst(2, 3)), False)
        expect(" 8. Short and long lists", eq(Lst(1, 2))(Lst(1, 2, 3)), False)
        expect(
            " 8. Same length lists with non-equal element",
            eq(Lst(1, 2, 3))(Lst(1, 2, 4)),
            False,
        )
        expect(" 8. Empty and non-empty lists", eq(Nil)(Lst(1, 2, 4)), False)
        expect(" 8. Non-empty and empty lists", eq(Lst(1, 2, 3))(Nil), False)

    test(eq, testing_eq)

    """
    ////////////////////////////////////////////////////////////////////////////////
    9.
    Implement the 'concat' function which concatenates two lists
    
    Type: concat :: [a] -> [a] -> [a]
    Signature: concat = as => bs => ...
    """

    def concat(lst1):
        return (
            lambda lst2: lst2
            if nil(lst1)
            else cons(head(lst1))(concat(tail(lst1))(lst2))
        )

    def testing_concat():
        expect(
            " 9. Concating two empty lists should be an empty list",
            concat(Nil)(Nil),
            Nil,
        )
        expect(
            " 9. Concating an empty list and a non-empty list should be the non-empty list",
            concat(Nil)(Lst(1, 2, 3)),
            Lst(1, 2, 3),
        )
        expect(
            " 9. Concating a non-empty list and an empty list should be the non-empty list",
            concat(Lst(1, 2, 3))(Nil),
            Lst(1, 2, 3),
        )
        expect(
            " 9. Concating two non-empty lists should be the second list appended to the first",
            concat(Lst(1, 2))(Lst(3, 4)),
            Lst(1, 2, 3, 4),
        )

    test(concat, testing_concat)

    """
    ////////////////////////////////////////////////////////////////////////////////
    10.
    Implement the 'reverse' function which reverses the list
    
    Type: reverse :: [a] -> [a]
    Signature: reverse = list => ...
    """

    def reverse(lst):
        return Nil if nil(lst) else cons(last(lst))(reverse(init(lst)))

    def testing_reverse():
        expect("10. Reversing an empty list is the empty list", reverse(Nil), Nil)
        expect(
            "10. Reversing a singleton list is the same list", reverse(Lst(1)), Lst(1)
        )
        expect("10. Reversing a list", reverse(Lst(1, 2, 3)), Lst(3, 2, 1))

    test(reverse, testing_reverse)

    """
    ////////////////////////////////////////////////////////////////////////////////
    11.
    Implement the 'func_filter' function which takes a predicate
    (a unary function returning a boolean) and a list and returns the list of
    those elements that satisfy the predicate
    
    Type: func_filter :: (a -> boolean) -> [a] -> [a]
    Signature: func_filter = p => list => ...
    """

    def func_filter(p):
        return (
            lambda lst: Nil
            if nil(lst)
            else func_filter(p)(tail(lst))
            if not p(head(lst))
            else cons(head(lst))(func_filter(p)(tail(lst)))
        )

    def testing_filter():
        expect("11. Filtering an empty list ", func_filter(constant(True))(Nil), Nil)
        expect("11. Filtering an empty list", func_filter(constant(False))(Nil), Nil)

        def odd(x):
            return x % 2 != 0

        expect(
            "11. Filtering odd numbers", func_filter(odd)(Lst(1, 2, 3, 4)), Lst(1, 3)
        )

    test(func_filter, testing_filter)

    """
    ////////////////////////////////////////////////////////////////////////////////
    12.
    Implement the 'func_map' function which returns a list obtained by applying the
    unary function f to each element in the list
    
    'f's signature: const f = e => ... where e is an element in the list
    
    Type: func_map :: (a -> b) -> [a] -> [b]
    Signature: func_map = f => list => ...
    """

    def square(x):
        return x ** 2

    def func_map(f):
        return (
            lambda lst: Nil if nil(lst) else cons(f(head(lst)))(func_map(f)(tail(lst)))
        )

    def testing_map():
        expect("12. Mapping over an empty list", func_map(square)(Nil), Nil)
        expect(
            "12. func_mapping with identity",
            func_map(identity)(Lst(1, 2, 3)),
            Lst(1, 2, 3),
        )
        expect("12. Mapping over a singleton list", func_map(square)(Lst(2)), Lst(4))
        expect("12. Mapping over a list", func_map(square)(Lst(1, 2, 3)), Lst(1, 4, 9))

    test(func_map, testing_map)

    """
    ////////////////////////////////////////////////////////////////////////////////
    13.
    Implement the 'foldl' function which takes a binary function f,
    a starting value z and a list.
    'foldl' reduces the list using the binary function from left to right.
    
    'f's signature: f = z => e => ...
    where z is the reduced value and e is the list element
    
    Type: foldl :: (b -> a -> b) -> b -> [a] -> b
    Signature: foldl = f => z => list => ...
    """

    def foldl(f):
        return (
            lambda accm: lambda lst: accm
            if nil(lst)
            else foldl(f)(f(accm)(head(lst)))(tail(lst))
        )

    def testing_foldl():
        def plus(a):
            return lambda b: a + b

        def minus(a):
            return lambda b: a - b

        expect(
            "13. Left folding an empty list to be the staring value",
            foldl(plus)(0)(Nil),
            0,
        )
        expect("13. Left folding a list with plus", foldl(plus)(0)(Lst(1, 2, 3)), 6)
        expect("13. Left folding a list with minus", foldl(minus)(0)(Lst(1, 2, 3)), -6)

    test(foldl, testing_foldl)

    """
    ////////////////////////////////////////////////////////////////////////////////
    14.
    Implement the 'foldr' function which takes a binary function f,
    a starting value z and a list.
    'foldr' reduces the list using the binary function from right to left.
    
    'f's signature: f = e => z => ...
    where e is the list element and z is the reduced value
    
    Type: foldr :: (a -> b -> b) -> b -> [a] -> b
    Signature: foldr = f => z => list => ...
    """

    def foldr(f):
        return (
            lambda accm: lambda lst: accm
            if nil(lst)
            else f(head(lst))(foldr(f)(accm)(tail(lst)))
        )

    def testing_foldr():
        def plus(a):
            return lambda b: a + b

        def minus(a):
            return lambda b: a - b

        expect(
            "14. Right folding an empty list to be the staring value",
            foldr(plus)(0)(Nil),
            0,
        )
        expect("14. Right folding a list with plus", foldr(plus)(0)(Lst(1, 2, 3)), 6)
        expect("14. Right folding a list with minus", foldr(minus)(0)(Lst(1, 2, 3)), 2)

    test(foldr, testing_foldr)

    """
    ////////////////////////////////////////////////////////////////////////////////
    15.
    Implement the 'copy' function which duplicates the list.
    Use the 'foldl' function
    
    Type: copy :: [a] -> [a]
    Signature: copy = list => ...
    """

    def copy(lst):
        return foldl(flip(cons))(Nil)(reverse(lst))

    def testing_copy():
        expect("15. Copy an empty list", copy(Nil), Nil)
        expect("15. Copy a singleton list", copy(Lst(1)), Lst(1))
        expect("15. Copy a list", copy(Lst(1, 2, 3)), Lst(1, 2, 3))

    test(copy, testing_copy)

    """
    ////////////////////////////////////////////////////////////////////////////////
    16.
    Implement the 'copy2' function which duplicates the list.
    Use the 'foldr' function
    
    Type: copy2 :: [a] -> [a]
    Signature: copy2 = list => ...
    """

    copy2 = foldr(cons)(Nil)

    def testing_copy2():
        expect("16. Copy an empty list", copy2(Nil), Nil)
        expect("16. Copy a singleton list", copy2(Lst(1)), Lst(1))
        expect("16. Copy a list", copy2(Lst(1, 2, 3)), Lst(1, 2, 3))

    test(copy2, testing_copy2)

    """
    ////////////////////////////////////////////////////////////////////////////////
    17.
    Implement the 'map2' function. It should be similar to 'map'.
    Use the 'foldr' function
    
    Type: map2 :: (a -> b) -> [a] -> [b]
    Signature: map2 = f => list => ...
    """

    def func_map2(f):
        return foldr(compose(cons)(f))(Nil)

    def testing_map2():
        expect("17. Mapping over an empty list", func_map2(square)(Nil), Nil)
        expect("17. Mapping over a singleton list", func_map2(square)(Lst(2)), Lst(4))
        expect("17. Mapping over a list", func_map2(square)(Lst(1, 2, 3)), Lst(1, 4, 9))

    test(func_map2, testing_map2)

    """
    ////////////////////////////////////////////////////////////////////////////////
    18.
    Implement the 'reverse2' function. It should be similar to 'reverse'.
    Use the 'foldl' function
    
    Type: reverse2 :: [a] -> [a]
    Signature: const reverse2 = list => ...
    """

    reverse2 = foldl(flip(cons))(Nil)

    def testing_reverse2():
        expect("18. Reversing an empty list is the empty list", reverse2(Nil), Nil)
        expect(
            "18. Reversing a singleton list is the same list", reverse2(Lst(1)), Lst(1)
        )
        expect("18. Reversing a list", reverse2(Lst(1, 2, 3)), Lst(3, 2, 1))

    test(reverse2, testing_reverse2)

    """
    For the following questions, we are introducing another data structure - pair

    A pair has two elements, the first and the second. To create a pair:
    
    const myPair = pair (1) (2) // This is the pair (1, 2)
    
    To extract the first element from the pair:
    
    const first = fst (myPair) // This will result in 1
    
    To extract the second element from the pair:
    
    const second = snd (myPair) // This will result in 2
    """

    """
    19.
    Implement the 'zip' function which takes two lists and returns a list of
    corresponding pairs. If one input list is short,
    excess elements of the longer list are discarded.
    
    Type: zip :: [a] -> [b] -> [(a, b)]
    Signature: zip = as => bs => ...
    """

    def zip_func(a_lst):
        return (
            lambda b_lst: Nil
            if nil(a_lst) or nil(b_lst)
            else cons(pair(head(a_lst))(head(b_lst)))(
                zip_func(tail(a_lst))(tail(b_lst))
            )
        )

    def testing_zip():
        expect("19. Zipping empty lists", zip_func(Nil)(Nil), Nil)
        expect("19. Zipping an empty list and a list", zip_func(Nil)(Lst(1, 2, 3)), Nil)
        expect("19. Zipping a list and an empty list", zip_func(Lst(1, 2, 3))(Nil), Nil)
        expect(
            "19. Zipping two same-length lists",
            zip_func(Lst(1, 2, 3))(Lst(10, 20, 30)),
            Lst(pair(1)(10), pair(2)(20), pair(3)(30)),
        )
        expect(
            "19. Zipping two lists, the first is shorter",
            zip_func(Lst(1, 2, 3))(Lst(10, 20, 30, 40)),
            Lst(pair(1)(10), pair(2)(20), pair(3)(30)),
        )
        expect(
            "19. Zipping two lists, the second is shorter",
            zip_func(Lst(1, 2, 3, 4))(Lst(10, 20, 30)),
            Lst(pair(1)(10), pair(2)(20), pair(3)(30)),
        )

    test(zip_func, testing_zip)

    """
    20.
    Implement the 'unzip' function which transforms a list of pairs into a
    list of first components and a list of second components.
    
    Type: unzip :: [(a, b)] -> ([a], [b])
    Signature: unzip = pairs => ...
    """

    def unzip_func(list_pairs):
        if nil(list_pairs):
            return pair(Nil)(Nil)
        else:
            tail_unzipped = unzip_func(tail(list_pairs))
            head_pair = head(list_pairs)
            return pair(cons(fst(head_pair))(fst(tail_unzipped)))(
                cons(snd(head_pair))(snd(tail_unzipped))
            )

    def testing_unzip():
        expect("20. unzipping empty lists", unzip_func(Nil), pair(Nil)(Nil))
        expect(
            "20. unzippint a list",
            unzip_func(Lst(pair(1)(10), pair(2)(20), pair(3)(30))),
            pair(Lst(1, 2, 3))(Lst(10, 20, 30)),
        )

    test(unzip_func, testing_unzip)


if __name__ == "__main__":
    main_program()
