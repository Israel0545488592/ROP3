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

        if len(col) < 1: raise ValueError('got no prefrences')

        get = (lambda key : col[key]) if isinstance(col, Mapping) else (lambda item : item)
        
        self.prioreties = { get(item) : len(col) -1 - priorty  for priorty, item in enumerate(col) }

        self.match = None


    def __getitem__(self, item) -> int: return self.prioreties[item]

    def __repr__(self) -> str: return self.prioreties.__repr__()

    def get_match(self, priorty: bool = True):
        
        if priorty:
            if self.match is None: return -1
            return self[self.match]
        return self.match

    def set_match(self, item) -> None: self.match = item


''' compact graph that acts as a manager of the 2 lists'''

class outype(ABC, Iterable):
    
    def __init__(self) -> None:
        super().__init__()

    #lazy initialization
    def build(self, first: Mapping[Any, Iterable], second: Mapping[Any, Iterable]):
        
        self.first_singles = { item : prefreances(first[item]) for item in first }
        self.second_singles = { item : prefreances(second[item]) for item in second }
        self.first_mached = {}
        self.second_mached = {}


    def __iter__(self, singles: bool, first: bool) -> Iterator:
        
        if first and singles:           return iter(self.first_singles)
        if first and not singles:       return iter(self.first_mached)
        if not first and singles:       return iter(self.second_singles)
        if not first and not singles:   return iter(self.second_mached)


    def get(self, item) -> prefreances:
        
        if item in self.first_singles:  return self.first_singles[item]
        if item in self.first_mached:   return self.first_mached[item]
        if item in self.second_singles: return self.second_singles[item]
        if item in self.second_mached:  return self.second_mached[item]

    def match(self, item, mate):

        item_prefs = self.get(item)
        mate_prefs = self.get(mate)

        if mate_prefs.get_match() < mate_prefs[item] and item_prefs.get_match() < item_prefs[mate]:

            old_match = mate_prefs.get_match(priorty = False)

            if old_match in self.first_mached:
                
                old_matchs_prefs =  self.get(old_match)
                old_matchs_prefs.set_match(None)
                self.first_singles[old_match] = old_matchs_prefs
                del self.first_mached[old_match]

            old_match = item_prefs.get_match(priorty = False)

            if old_match in self.second_mached:
                
                old_matchs_prefs =  self.get(old_match)
                old_matchs_prefs.set_match(None)
                self.second_singles[old_match] = old_matchs_prefs
                del self.second_mached[old_match]

            mate_prefs.set_match(item)
            item_prefs.set_match(mate)
            
            if item in self.first_singles:
                self.first_mached[item] = item_prefs
                del self.first_singles[item]
            if mate in self.second_singles:
                self.second_mached[mate] = mate_prefs
                del self.second_singles[mate]
            if item in self.second_singles:
                self.second_mached[item] = item_prefs
                del self.second_singles[item]
            if mate in self.first_singles:
                self.first_mached[mate] = mate_prefs
                del self.first_singles[mate]

            return True

        return False

    @abstractclassmethod
    def extract_result(self):   pass


class setesfaction(outype):

    def __init__(self,) -> None:
        super().__init__()


    def extract_result(self):

        res = {**self.first_mached, **self.second_mached}

        return reduce(lambda x, y: x + y, [prefs.get_match() for prefs in res.values()]) / len(res)


class matches(outype):

    def __init__(self) -> None:
        super().__init__()


    def extract_result(self):
        return [(item, prefs.get_match(priorty = False)) for item, prefs in self.first_mached.items()]