from python.list import cons, head, tail, Nil, Lst
from python.test import test, expect
from python.functions import flip, compose, identity, constant


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

    init = None

    def testing_init():
        expect(
            "2. The first element in the init of a list", head(init(Lst(1, 2, 3))), 1
        )
        expect(
            "2. The second element in the init of a list", head(init(Lst(1, 2, 3))), 2
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

    last = None

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
    elem = None

    def testing_elem():
        expect(" 4. Element should not be found in an empty list", elem(1)(Nil), False)
        expect(" 4. Existing element is first", elem(1)(Lst(1, 2, 3)), True)
        expect(" 4. Existing element is last", elem(1)(Lst(3, 2, 1)), True)
        expect(" 4. Existing element in a singleton list", elem(1)(Lst(1)), True)
        expect(" 4. Non-existing element", elem(4)(Lst(1, 2, 3)), False)

    test(elem, testing_init)

    """
    ////////////////////////////////////////////////////////////////////////////////
    5.
    Implement the 'length' function which returns the number of elements in the list
    
    Type: length :: [a] -> number
    Signature: const length = list => ...
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


if __name__ == "__main__":
    main_program()
