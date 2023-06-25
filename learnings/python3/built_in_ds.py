from collections import namedtuple


def list_comprehensions():
    # create a list without comprehensions
    nick_name = 'cricri'
    list_of_char = []
    for letter in nick_name:
        list_of_char.append(letter)
    print(list_of_char)

    # create a list with comprehensions
    nick_name = 'cricri'
    list_of_char = [letter for letter in nick_name]  # Adding elements from letters to alphabets

    print(list_of_char)

    # filtering comprehensions
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even = [number for number in numbers if number % 2 == 0]
    print(even)

    # Enriched iterations with list comprehension
    even = [2, 4, 6, 8, 10]
    odd = [1, 3, 5, 7, 9]

    tuple_number = [(number1, number2) for number1 in even for number2 in odd]
    print(tuple_number)


def pair():
    # Unpacking the tuples
    fruits = [('banana', 'yellow', 10), ('apple', 'red', 19)]
    for name, _, _ in fruits:
        print(name)

    def add(a, b):
        return a + b

    numbers = (1, 2)
    result = add(*numbers)  # Unpacking numbers with * : add(1,2)
    print(result)


def named_tuple():
    Fruit = namedtuple('Fruit', 'name color price')
    f1 = Fruit("apple", "red", 29)
    f2 = Fruit("banana", "yellow", 29)

    print(f1.name, f1.color, f1.price)
    print(f2.name, f2.color, f2.price)


def stack_queue_implementation():
    # list type does make a good stack, because append() adds an element at the end
    # and pop() deletes an element from the end, in amortized time of O(1)
    # But the list is a terrible choice to make a queue because inserting at
    # and deleting from the beginning requires shifting all the elements by one,
    # requiring O(n) (dynamic array implementation)
    stack = ["hello ", "world ", "cricri"]
    stack.append("blub")
    stack.pop()
    print("stack with a list : " + str(stack))

    queue = ["hello ", "world ", "cricri"]
    queue.append("blub")
    queue.pop(0)
    print("queue with list : " + str(queue))

    # deque is like a double-ended queue that lets you add or remove elements from either end.
    # It takes O(1) time for both operations, whether it’s a stack or a queue implementation.
    # But backend implementation of deque is a doubly-linked list,
    # which is why random access in the worst case is O(n) unlike the list.
    from collections import deque
    stack = deque()
    stack.append("hello ")
    stack.append("world ")
    stack.append("cricri ")
    stack.append("blub")
    stack.pop()
    print("stack with deque : " + str(stack))

    queue = deque()
    queue.append("hello ")
    queue.append("world ")
    queue.append("cricri")
    queue.append("blub")
    queue.popleft()
    print("queue with deque : " + str(queue))


def set_exploration():
    # MUTABLE
    prime = {2, 3, 5, 7, 11}
    odd = {1, 3, 5, 7, 9}
    odd.add(11)
    print('Union = ', odd.union(prime))
    print('Intersection = ', odd.intersection(prime))

    # IMMUTABLE
    odd = frozenset({1, 3, 5, 7, 9, 11})
    even = frozenset({2, 4, 6, 8, 10, 12})

    # Making dictionary with frozensets as keys
    d = {odd: 'odd', even: 'even'}
    print(d[odd])
    print(d[even])

    # Making set with frozensets
    numbers = set()
    numbers.add(odd)
    numbers.add(even)
    print(numbers)


def counter_exploration():
    from collections import Counter
    c1 = Counter('Python 3: An In-Depth Exploration')  # Using iteratable
    c2 = Counter({'numbers': 10, 'letters': 26})  # Using mapping

    # Finding number of occurances
    print(c1['o'])
    print(c2['numbers'])
    print(c2['alphabets'])


def dictionary_exploration():
    print("")


if __name__ == '__main__':
    # list_comprehensions()
    # pair()
    # named_tuple()
    # stack_queue_implementation()
    # set_exploration()
    counter_exploration()
