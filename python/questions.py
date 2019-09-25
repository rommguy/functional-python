from python.list import cons, head, tail, Nil, Lst
from python.test import TestApi
from python.functions import flip, compose, identity, constant
from python.pair import pair, fst, snd


def main_program():
    """
  In this test, a basic implementation of a linked list data structure is given (called list_f)

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
  'Nil' is the empty list_f. This is how you use 'Nil':

  my_empty_list = Nil

  - cons -
  Type: cons :: a -> [a] -> [a]

  'cons' is the list_f constructor. It is a function that takes a 'head' and 'tail'
  and returns a new list_f. The 'head' is any value and the 'tail' is
  a list_f. This is how you use 'cons':

  my_singleton_list = cons (2) (Nil) // This will return the list_f: [2]
  my_two_element_list = cons (1) (my_singleton_list) // This will return the list_f: [1, 2]
  my_three_element_list = cons (1) (cons (2) (cons (3) (Nil))) // This will return the list_f: [1, 2, 3]

  - head -
  Type: head :: [a] -> a

  'head' is a function that takes a non-empty list_f and returns its head. The head
  is the first element in the list_f. This is how you use 'head':

  my_head = head (my_three_element_list) // This will return 1
  no_head = head (Nil) // This will throw an error since the list_f is empty

  - tail -
  Type: tail :: [a] -> [a]

  'tail' is a function that takes a non-empty list_f and returns its tail. The tail
  is a list_f with all elements except for the first one. This is how you use 'tail':

  myTail = tail (my_three_element_list) // This will return the list_f: [2, 3]
  noTail = tail (Nil) // This will throw an error since the list_f is empty

  As you can see, the following will hold for any non-empty list_f l:

  cons (head (l)) (tail (l)) === l

  --------------------------------------------------------------------------------

  Each question has a short description followed by some tests.
  To start implementing the question functions, run this python file and open the index.html file in chrome.
  Go over the questions one by one and implement the required function.
  When you are done with a question, run this file again and refresh chrome - make sure the tests pass.
  The html page will present the test results in green for success and red for
  failure, for the last time questions.py was executed.

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

  'constant' is the constant function, always returns the initial value it was given.

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
    // Implement the 'nil' function which returns true if the list_f is Nil and false otherwise
    //
    // Type: nil :: [a] -> boolean
    // Signature: nil = list_f => ...
    """

    def nil(list_f):
        return list_f == Nil

    def testing_nil():
        expect("1. nil on empty list_f", nil(Nil), True)
        expect("1. nil on empty list_f", nil(Lst(1, 2, 3)), False)

    test(nil, testing_nil)

    """
    ////////////////////////////////////////////////////////////////////////////////
    2.
     Implement the 'init' function which returns all the elements of a
     list_f except the last one. The list_f must be non-empty
    
     Type: init :: [a] -> [a]
     Signature: init = list_f => ...
    """

    def init(list_f):
        return (lambda t: Nil if nil(t) else cons(head(list_f))(init(t)))(tail(list_f))

    def testing_init():
        expect("2. The first element in the init of a list_f", head(init(Lst(1, 2, 3))), 1)
        expect("2. The second element in the init of a list_f", head(tail(init(Lst(1, 2, 3)))), 2)
        expect("2. The init length should be 2", tail(tail(init(Lst(1, 2, 3)))), Nil)

    test(init, testing_init)

    """
    ////////////////////////////////////////////////////////////////////////////////
     3.
     Implement the 'last' function which returns the last element in the list_f
    
     Type: last :: [a] -> a
     Signature: last = list_f => ...
    """

    def last(list_f):
        return (lambda t: head(list_f) if nil(t) else last(t))(tail(list_f))

    def testing_last():
        expect("3. tail of a list_f", last(Lst(1, 2, 3)), 3)
        expect("3. tail of a singleton list_f", last(Lst(1)), 1)

    test(last, testing_last)

    """
    ////////////////////////////////////////////////////////////////////////////////
     4.
     Implement the 'elem' function which return true if the element occurs in the
     list_f and false otherwise
    
     Type: elem :: a -> [a] -> boolean
     Signature: elem = e => list_f => ...
    """

    def elem(e):
        def inner(list_f):
            if nil(list_f):
                return False
            elif head(list_f) == e:
                return True
            else:
                return elem(e)(tail(list_f))

        return inner

    def testing_elem():
        expect(" 4. Element should not be found in an empty list_f", elem(1)(Nil), False)
        expect(" 4. Existing element is first", elem(1)(Lst(1, 2, 3)), True)
        expect(" 4. Existing element is last", elem(1)(Lst(3, 2, 1)), True)
        expect(" 4. Existing element in a singleton list_f", elem(1)(Lst(1)), True)
        expect(" 4. Non-existing element", elem(4)(Lst(1, 2, 3)), False)

    test(elem, testing_elem)

    """
    ////////////////////////////////////////////////////////////////////////////////
    5.
    Implement the 'length' function which returns the number of elements in the list_f
    
    Type: length :: [a] -> number
    Signature: length = list_f => ...
    """

    def length(list_f):
        return 0 if nil(list_f) else 1 + length(tail(list_f))

    def testing_length():
        expect(" 5. The length of an empty list_f should be 0", length(Nil), 0)
        expect(" 5. The length of a singleton list_f should be 1", length(Lst(1)), 1)
        expect(" 5. The length of a list_f with 3 elements should be 3", length(Lst(1, 2, 3)), 3)

    test(length, testing_length)

    """
    ////////////////////////////////////////////////////////////////////////////////
    6.
    Implement the 'take' function which return the prefix of list_f of length n.
    If n > length(list_f), return list_f
    
    Type: take :: number -> [a] -> [a]
    Signature: take = n => list_f => ...
    """

    def take(n):
        return (
            lambda list_f: Nil
            if nil(list_f) or n == 0
            else cons(head(list_f))(take(n - 1)(tail(list_f)))
        )

    def testing_take():
        expect(" 6. Taking 0 from Nil", take(0)(Nil), Nil)
        expect(" 6. Taking 3 from Nil", take(3)(Nil), Nil)
        expect(" 6. Taking 0 from a list_f of 3", take(0)(Lst(1, 2, 3)), Nil)
        expect(" 6. Taking 1 from a list_f of 3", take(1)(Lst(1, 2, 3)), Lst(1))
        expect(" 6. Taking 2 from a list_f of 3", take(2)(Lst(1, 2, 3)), Lst(1, 2))
        expect(" 6. Taking 3 from a list_f of 3", take(3)(Lst(1, 2, 3)), Lst(1, 2, 3))
        expect(" 6. Taking 4 from a list_f of 3", take(4)(Lst(1, 2, 3)), Lst(1, 2, 3))

    test(take, testing_take)

    """
    ////////////////////////////////////////////////////////////////////////////////
    7.
    Implement the 'drop' function which returns the suffix of list_f after the first n elements.
    If n > length(list_f), return Nil
    
    Type: drop :: number -> [a] -> [a]
    Signature: drop = n => list_f => ...
    """

    def drop(n):
        return lambda list_f: list_f if nil(list_f) or n == 0 else drop(n - 1)(tail(list_f))

    def testing_drop():
        expect(" 7. Dropping 0 from Nil", drop(0)(Nil), Nil)
        expect(" 7. Dropping 3 from Nil", drop(3)(Nil), Nil)
        expect(" 7. Dropping 0 from a list_f of 3", drop(0)(Lst(1, 2, 3)), Lst(1, 2, 3))
        expect(" 7. Dropping 1 from a list_f of 3", drop(1)(Lst(1, 2, 3)), Lst(2, 3))
        expect(" 7. Dropping 2 from a list_f of 3", drop(2)(Lst(1, 2, 3)), Lst(3))
        expect(" 7. Dropping 3 from a list_f of 3", drop(3)(Lst(1, 2, 3)), Nil)
        expect(" 7. Dropping 4 from a list_f of 3", drop(4)(Lst(1, 2, 3)), Nil)

    test(drop, testing_drop)

    """
    // 8.
    Implement the 'eq' function which returns 'true' if the lists are equal
    and 'false' otherwise
    
    Type: eq :: [a] -> [a] -> boolean
    Signature: eq = as => bs => ...
    """

    def eq(func_list1):
        return (
            lambda func_list2: True
            if nil(func_list1)
            and nil(func_list2)
            or not nil(func_list1)
            and not nil(func_list2)
            and head(func_list1) == head(func_list2)
            and eq(tail(func_list1))(tail(func_list2))
            else False
        )

    def testing_eq():
        expect(" 8. Empty list_f equality", eq(Nil)(Nil), True)
        expect(" 8. Non-empty list_f equality", eq(Lst(1, 2, 3))(Lst(1, 2, 3)), True)
        expect(" 8. Long and short lists", eq(Lst(1, 2, 3))(Lst(2, 3)), False)
        expect(" 8. Short and long lists", eq(Lst(1, 2))(Lst(1, 2, 3)), False)
        expect(
            " 8. Same length lists with non-equal element", eq(Lst(1, 2, 3))(Lst(1, 2, 4)), False
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

    def concat(func_list1):
        return (
            lambda func_list2: func_list2
            if nil(func_list1)
            else cons(head(func_list1))(concat(tail(func_list1))(func_list2))
        )

    def testing_concat():
        expect(" 9. Concatenating two empty lists should be an empty list_f", concat(Nil)(Nil), Nil)
        expect(
            " 9. Concatenating an empty list_f and a non-empty list_f should be the non-empty list_f",
            concat(Nil)(Lst(1, 2, 3)),
            Lst(1, 2, 3),
        )
        expect(
            " 9. Concatenating a non-empty list_f and an empty list_f should be the non-empty list_f",
            concat(Lst(1, 2, 3))(Nil),
            Lst(1, 2, 3),
        )
        expect(
            " 9. Concatenating two non-empty lists should be the second list_f appended to the first",
            concat(Lst(1, 2))(Lst(3, 4)),
            Lst(1, 2, 3, 4),
        )

    test(concat, testing_concat)

    """
    ////////////////////////////////////////////////////////////////////////////////
    10.
    Implement the 'reverse' function which reverses the list_f
    
    Type: reverse :: [a] -> [a]
    Signature: reverse = list_f => ...
    """

    def reverse(list_f):
        return Nil if nil(list_f) else cons(last(list_f))(reverse(init(list_f)))

    def testing_reverse():
        expect("10. Reversing an empty list_f is the empty list_f", reverse(Nil), Nil)
        expect("10. Reversing a singleton list_f is the same list_f", reverse(Lst(1)), Lst(1))
        expect("10. Reversing a list_f", reverse(Lst(1, 2, 3)), Lst(3, 2, 1))

    test(reverse, testing_reverse)

    """
    ////////////////////////////////////////////////////////////////////////////////
    11.
    Implement the 'filter_f' function which takes a predicate
    (a unary function returning a boolean) and a list_f and returns the list_f of
    those elements that satisfy the predicate
    
    Type: filter_f :: (a -> boolean) -> [a] -> [a]
    Signature: filter_f = p => list_f => ...
    """

    def filter_f(p):
        return (
            lambda list_f: Nil
            if nil(list_f)
            else filter_f(p)(tail(list_f))
            if not p(head(list_f))
            else cons(head(list_f))(filter_f(p)(tail(list_f)))
        )

    def testing_filter():
        expect("11. Filtering an empty list_f ", filter_f(constant(True))(Nil), Nil)
        expect("11. Filtering an empty list_f", filter_f(constant(False))(Nil), Nil)

        def odd(x):
            return x % 2 != 0

        expect("11. Filtering odd numbers", filter_f(odd)(Lst(1, 2, 3, 4)), Lst(1, 3))

    test(filter_f, testing_filter)

    """
    ////////////////////////////////////////////////////////////////////////////////
    12.
    Implement the 'map_f' function which returns a list_f obtained by applying the
    unary function f to each element in the list_f
    
    'f's signature: const f = e => ... where e is an element in the list_f
    
    Type: map_f :: (a -> b) -> [a] -> [b]
    Signature: map_f = f => list_f => ...
    """

    def square(x):
        return x ** 2

    def map_f(f):
        return lambda list_f: Nil if nil(list_f) else cons(f(head(list_f)))(map_f(f)(tail(list_f)))

    def testing_map():
        expect("12. Mapping over an empty list_f", map_f(square)(Nil), Nil)
        expect("12. func_mapping with identity", map_f(identity)(Lst(1, 2, 3)), Lst(1, 2, 3))
        expect("12. Mapping over a singleton list_f", map_f(square)(Lst(2)), Lst(4))
        expect("12. Mapping over a list_f", map_f(square)(Lst(1, 2, 3)), Lst(1, 4, 9))

    test(map_f, testing_map)

    """
    ////////////////////////////////////////////////////////////////////////////////
    13.
    Implement the 'foldl' function which takes a binary function f,
    a starting value z and a list_f.
    'foldl' reduces the list_f using the binary function from left to right.
    
    'f's signature: f = z => e => ...
    where z is the reduced value and e is the list_f element
    
    Type: foldl :: (b -> a -> b) -> b -> [a] -> b
    Signature: foldl = f => z => list_f => ...
    """

    def foldl(f):
        return (
            lambda accm: lambda list_f: accm
            if nil(list_f)
            else foldl(f)(f(accm)(head(list_f)))(tail(list_f))
        )

    def testing_foldl():
        def plus(a):
            return lambda b: a + b

        def minus(a):
            return lambda b: a - b

        expect("13. Left folding an empty list_f to be the staring value", foldl(plus)(0)(Nil), 0)
        expect("13. Left folding a list_f with plus", foldl(plus)(0)(Lst(1, 2, 3)), 6)
        expect("13. Left folding a list_f with minus", foldl(minus)(0)(Lst(1, 2, 3)), -6)

    test(foldl, testing_foldl)

    """
    ////////////////////////////////////////////////////////////////////////////////
    14.
    Implement the 'foldr' function which takes a binary function f,
    a starting value z and a list_f.
    'foldr' reduces the list_f using the binary function from right to left.
    
    'f's signature: f = e => z => ...
    where e is the list_f element and z is the reduced value
    
    Type: foldr :: (a -> b -> b) -> b -> [a] -> b
    Signature: foldr = f => z => list_f => ...
    """

    def foldr(f):
        return (
            lambda accm: lambda list_f: accm
            if nil(list_f)
            else f(head(list_f))(foldr(f)(accm)(tail(list_f)))
        )

    def testing_foldr():
        def plus(a):
            return lambda b: a + b

        def minus(a):
            return lambda b: a - b

        expect("14. Right folding an empty list_f to be the staring value", foldr(plus)(0)(Nil), 0)
        expect("14. Right folding a list_f with plus", foldr(plus)(0)(Lst(1, 2, 3)), 6)
        expect("14. Right folding a list_f with minus", foldr(minus)(0)(Lst(1, 2, 3)), 2)

    test(foldr, testing_foldr)

    """
    ////////////////////////////////////////////////////////////////////////////////
    15.
    Implement the 'copy' function which duplicates the list_f.
    Use the 'foldl' function
    
    Type: copy :: [a] -> [a]
    Signature: copy = list_f => ...
    """

    def copy(list_f):
        return foldl(flip(cons))(Nil)(reverse(list_f))

    def testing_copy():
        expect("15. Copy an empty list_f", copy(Nil), Nil)
        expect("15. Copy a singleton list_f", copy(Lst(1)), Lst(1))
        expect("15. Copy a list_f", copy(Lst(1, 2, 3)), Lst(1, 2, 3))

    test(copy, testing_copy)

    """
    ////////////////////////////////////////////////////////////////////////////////
    16.
    Implement the 'copy2' function which duplicates the list_f.
    Use the 'foldr' function
    
    Type: copy2 :: [a] -> [a]
    Signature: copy2 = list_f => ...
    """

    copy2 = foldr(cons)(Nil)

    def testing_copy2():
        expect("16. Copy an empty list_f", copy2(Nil), Nil)
        expect("16. Copy a singleton list_f", copy2(Lst(1)), Lst(1))
        expect("16. Copy a list_f", copy2(Lst(1, 2, 3)), Lst(1, 2, 3))

    test(copy2, testing_copy2)

    """
    ////////////////////////////////////////////////////////////////////////////////
    17.
    Implement the 'map2' function. It should be similar to 'map'.
    Use the 'foldr' function
    
    Type: map2 :: (a -> b) -> [a] -> [b]
    Signature: map2 = f => list_f => ...
    """

    def func_map2(f):
        return foldr(compose(cons)(f))(Nil)

    def testing_map2():
        expect("17. Mapping over an empty list_f", func_map2(square)(Nil), Nil)
        expect("17. Mapping over a singleton list_f", func_map2(square)(Lst(2)), Lst(4))
        expect("17. Mapping over a list_f", func_map2(square)(Lst(1, 2, 3)), Lst(1, 4, 9))

    test(func_map2, testing_map2)

    """
    ////////////////////////////////////////////////////////////////////////////////
    18.
    Implement the 'reverse2' function. It should be similar to 'reverse'.
    Use the 'foldl' function
    
    Type: reverse2 :: [a] -> [a]
    Signature: const reverse2 = list_f => ...
    """

    reverse2 = foldl(flip(cons))(Nil)

    def testing_reverse2():
        expect("18. Reversing an empty list_f is the empty list_f", reverse2(Nil), Nil)
        expect("18. Reversing a singleton list_f is the same list_f", reverse2(Lst(1)), Lst(1))
        expect("18. Reversing a list_f", reverse2(Lst(1, 2, 3)), Lst(3, 2, 1))

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
    Implement the 'zip_f' function which takes two lists and returns a list_f of
    corresponding pairs. If one input list_f is short,
    excess elements of the longer list_f are discarded.
    
    Type: zip_f :: [a] -> [b] -> [(a, b)]
    Signature: zip_f = as => bs => ...
    """

    def zip_f(a_lst_f):
        return (
            lambda b_lst_f: Nil
            if nil(a_lst_f) or nil(b_lst_f)
            else cons(pair(head(a_lst_f))(head(b_lst_f)))(zip_f(tail(a_lst_f))(tail(b_lst_f)))
        )

    def testing_zip():
        expect("19. Zipping empty lists", zip_f(Nil)(Nil), Nil)
        expect("19. Zipping an empty list_f and a list_f", zip_f(Nil)(Lst(1, 2, 3)), Nil)
        expect("19. Zipping a list_f and an empty list_f", zip_f(Lst(1, 2, 3))(Nil), Nil)
        expect(
            "19. Zipping two same-length lists",
            zip_f(Lst(1, 2, 3))(Lst(10, 20, 30)),
            Lst(pair(1)(10), pair(2)(20), pair(3)(30)),
        )
        expect(
            "19. Zipping two lists, the first is shorter",
            zip_f(Lst(1, 2, 3))(Lst(10, 20, 30, 40)),
            Lst(pair(1)(10), pair(2)(20), pair(3)(30)),
        )
        expect(
            "19. Zipping two lists, the second is shorter",
            zip_f(Lst(1, 2, 3, 4))(Lst(10, 20, 30)),
            Lst(pair(1)(10), pair(2)(20), pair(3)(30)),
        )

    test(zip_f, testing_zip)

    """
    20.
    Implement the 'unzip' function which transforms a list_f of pairs into a
    list_f of first components and a list_f of second components.
    
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
            "20. unzipping a list_f",
            unzip_func(Lst(pair(1)(10), pair(2)(20), pair(3)(30))),
            pair(Lst(1, 2, 3))(Lst(10, 20, 30)),
        )

    test(unzip_func, testing_unzip)


if __name__ == "__main__":
    main_program()
