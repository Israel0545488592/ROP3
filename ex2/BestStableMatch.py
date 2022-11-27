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

import custom_input as inp
import custom_output as out
from typing import Callable, List


MatchingAlgo = Callable[[out.connections]]


def StableMatching(algo: MatchingAlgo, first: List[List], second: List[List], output: out.connections, **kwargs):

    prioreties_first = [inp.prefreances(str(n), lambda item : l.index(item)) for n, l in enumerate(first)]
    prioreties_second = [inp.prefreances(str(n), lambda item : l.index(item)) for n, l in enumerate(second)]

    graph = output.__init__((prioreties_first, prioreties_second))

    algo(graph)

    return graph.extract_matching