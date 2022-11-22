'''

    subsetsum_req is agenerator for all subsets of an iterable
    with a specific sum, it searches requrcivly throgh the different options (DFS)
    BUT: it gets as arguments the remaining sum to search for and an iterator.
    Thus O(1) - time complexty (for each yeild), at any given moment
    the stack may hold O(n) iteraors where n is the size of the input (O(n) memory comlexty)
    this function deals with posetive items only

    PowerSetSum is a generator for all subsets sorted by sum using subsetsum_req

    small note: for collections that support bi-directional iterators
    the function can be upgraded s.t it woild use 1 iterator (absolutly most efficient)
'''


from typing import Union, Iterable, Iterator
from copy import copy


def PowerSetSum(col: Iterable) -> list:

    for setsum in range(sum(col) +1):
        for subset in bounded_subsets(col, setsum):
            yield subset


def bounded_subsets(col: Iterable, sum: Union[int, float]) -> list:   

    if sum == 0: yield []   # the empty set

    for subset in subsetsum_req(sum, iter(col)):   yield subset


def subsetsum_req(sum: Union[int, float], itr: Iterator) -> list:

    while True:

        try:

            val = itr.__next__()

            if val == sum:  yield [val]
            if sum >= val:
                for subset in subsetsum_req(sum - val, copy(itr)):  yield [val] + subset
            
        except StopIteration:
            break



if __name__ == '__main__':

    for subset in PowerSetSum(range(5)):    print(subset)


# todo: tests, git