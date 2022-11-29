'''
    The Stable Match Problome:

    input: 2 disjoint lists A & B.
    each element in A has a priorty bijection : B -> range(len(B))
    that is, prefrences.
    ( complete bipartite weighted hyper-graph )

    output: a stable matching: a perfect matching s.t:
    there is no couple that prefers to break its existing matchings
    in favor of one another
    
    This is an ettempt on an implementation of the strategy design pattern
    revolving this problome.
    
    I build costum I/O data structures for: hiding details,
    saving memory (FlyWeight design pattern) and versatilty

    I implement 2 algorithms: propose-reject (gale shapley)
    
    And an origonal (as far as I am awere) algorithm of my own
    It is somewhat greedy and I sespect it may usually yeild a stable match
    tha stesfies the participants better
'''


from custom_output import outype
from typing import Mapping, Callable, Any, Iterable
from numpy.random import randint
from itertools import permutations

MatchingAlgo = Callable[[outype], Any]


def StableMatching(algo: MatchingAlgo, first: Mapping[Any, Iterable], second: Mapping[Any, Iterable], graph: outype, **kwargs):

    graph.build(first, second)

    algo(graph, **kwargs)

    return graph.extract_result()


def RandomTestRuns(algo: MatchingAlgo, graph: outype, size: int, **kwargs):

    first  = list(randint(0, 10*size, size))
    second = list(randint(-10*size, 0, size))

    first_prefs = {item : prefs for item, prefs in zip(first, permutations(second))}
    second_prefs = {item : prefs for item, prefs in zip(second, permutations(first))}

    return StableMatching(algo, first_prefs, second_prefs, graph, **kwargs)



def propose_regect(graph: outype):

    while True:

        try:

            item = next(graph.__iter__(singles = True, first = True))
            mate = next(graph.__iter__(singles = True, first = False))
            if graph.match(item, mate): stable = False
        
        except StopIteration:
            break


def MyGreedy(graph: outype):    pass