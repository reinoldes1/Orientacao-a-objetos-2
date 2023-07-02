from abc import ABC #abastract base classes

from collections.abc import MutableSequence
from numbers import Complex

class Numero (Complex):
    def __getitem__(self, item):
        super().__getitem__()

filmes = Numero ()

class Playlist(MutableSequence):
    pass

filmes = Playlist()