''' 
    Defining custom data structures that act as an interface
    for algorithms to use.
    They support several servecies for different types of output
    So any algorithm would need to be written only once
'''

from typing import Mapping, Iterable, Iterator, Any
from abc import ABC, abstractclassmethod
from functools import reduce


class prefreances(Iterable):

    # generic parser to a consistent data structure to work with
    def __init__(self, col: Iterable) -> None:

        get = lambda key : col[key] if isinstance(col, Mapping) else lambda item : item
        
        self.prioreties = { get(item) : priorty  for priorty, item in enumerate(col) }

        self.match = -1


    def __len__(self) -> int: return len(self.prioreties)

    def __getitem__(self, item) -> int: return self.prioreties[item]

    @property
    def match(self): return self.match

    @match.setter
    def match(self, item) -> None: self.match = self.prioreties[item]


''' compact graph that acts as a manager of the 2 lists'''

class outype(ABC, Iterable):
    
    def __init__(self) -> None:
        super().__init__()

    #lazy initialization
    def build(self, first: Mapping[Any, Iterable], second: Mapping[Any, Iterable]):
        
        self.first_singles = { item : prefreances(item, first[item]) for item in first }
        self.second = { item : prefreances(item, second[item]) for item in second }
        self.first_mached = {}


    def __iter__(self, singles: bool, first: bool = True) -> Iterator:
        
        if first and singles:     return iter(self.first_singles.values())
        if first and not singles: return iter(self.first_mached.values())
        else:                     return iter(self.second.values)                
        

    def match(self, item: prefreances, mate: prefreances):

        if mate.match() < mate[item]:

            mate.match().match(-1)
            mate.match(mate[item])
            return True
        return False

    @abstractclassmethod
    def extract_result(self):   pass


class outype_setesfaction(outype):

    def __init__(self, first: Mapping[Any, Iterable], second: Mapping[Any, Iterable]) -> None:
        super().__init__(first, second)


    def extract_result(self):
        return reduce(sum, [(item, item[item.match()]) for item in self.first_mached]) / len(self.first_mached)




class outype_matches(outype):

    def __init__(self, first: Mapping[Any, Iterable], second: Mapping[Any, Iterable]) -> None:
        super().__init__(first, second)


    def extract_result(self):
        return [(item, item.match()) for item in self.first_mached]