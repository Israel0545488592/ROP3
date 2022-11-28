''' 
    Defining custom data structures that act as an interface
    for algorithms to use.
    They support several servecies for different types of output
    So any algorithm would need to be written only once
'''

from typing import Mapping, Iterable, Iterator, Any
from abc import ABC, abstractclassmethod
from functools import reduce


class prefreances():

    # generic parser to a consistent data structure to work with
    def __init__(self, col: Iterable) -> None:

        get = (lambda key : col[key]) if isinstance(col, Mapping) else (lambda item : item)
        
        self.prioreties = { get(item) : priorty  for priorty, item in enumerate(col) }

        self.match = -1


    def __getitem__(self, item) -> int: return self.prioreties[item]

    def __repr__(self) -> str: return self.prioreties.__repr__()

    def get_match(self): return self.match

    def set_match(self, item) -> None: self.match = self.prioreties[item]


''' compact graph that acts as a manager of the 2 lists'''

class outype(ABC, Iterable):
    
    def __init__(self) -> None:
        super().__init__()

    #lazy initialization
    def build(self, first: Mapping[Any, Iterable], second: Mapping[Any, Iterable]):
        
        self.first_singles = { item : prefreances(first[item]) for item in first }
        self.second = { item : prefreances(second[item]) for item in second }
        self.first_mached = {}


    def __iter__(self, singles: bool, first: bool = True) -> Iterator:
        
        if first and singles:     return iter(self.first_singles)
        if first and not singles: return iter(self.first_mached)
        else:                     return iter(self.second)


    def get(self, item, singles: bool = False, first: bool = False) -> prefreances:
        
        if first and singles:     return self.first_singles[item]
        if first and not singles: return self.first_mached[item]
        else:                     return self.second[item]

    def match(self, item, mate):

        item_prefs = self.get(item, first = True, singles = True)
        mate_prefs = self.get(mate)

        if mate_prefs.get_match() < mate_prefs[item]:

            old_match = mate_prefs.get_match()

            if old_match in self.first_mached:
                
                old_matchs_prefs =  self.get(item, first = True, singles = True)
                old_matchs_prefs.set_match(-1)
                self.first_singles[old_match] = old_matchs_prefs
                del self.first_mached[old_match]

            mate_prefs.set_match(item)
            item_prefs.set_match(mate)
            self.first_mached[item] = item_prefs
            del self.first_singles[item]
            return True

        return False

    @abstractclassmethod
    def extract_result(self):   pass


class outype_setesfaction(outype):

    def __init__(self,) -> None:
        super().__init__()


    def extract_result(self):
        return reduce(sum, [(item, prefs.get_match()) for item, prefs in self.first_mached.items()]) / len(self.first_mached)


class outype_matches(outype):

    def __init__(self) -> None:
        super().__init__()


    def extract_result(self):
        return [(item, prefs[prefs.get_match()]) for item, prefs in self.first_mached.items()]