from custom_input import *
from typing import List
from abc import ABC, abstractclassmethod


class connections(ABC, Iterable):

    def __init__(self) -> None:
        super().__init__()
    

    #lazy initialization
    def start(self, first: List[prefreances], second: List[prefreances]) -> None:
        
        self.first = first
        self.second = second

    def __iter__(self, first: bool = True) -> Iterator:
        
        if first:   return iter(self.first)
        else:       return iter(self.second)

    @abstractclassmethod
    def match(self, item_first, item_second):
        pass


class cnnections_setesfaction(connections): pass
class connections_matches(connections):     pass