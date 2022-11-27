''' 

    Defining the input data structure, prefrences list
    Trying to be as generic as possible

'''

from typing import Collection, Mapping, Iterable, Iterator, Callable, Any


class prefreances(Iterable):

    def __init__(self, name: str, col: Collection,  priorty: Callable[[Any], int]) -> None:

        items = col.values() if isinstance(col, Mapping) else col
        
        self.name = name
        self.prioreties = { priorty(items) : item for item in items }

    def __len__(self) -> int: return len(self.prioreties)

    def __getitem__(self, priorty: int): return self.prioreties(priorty)

    def __iter__(self) -> Iterator: return iter(self.prioreties)

    @property
    def get_name(self) -> str: return self.name