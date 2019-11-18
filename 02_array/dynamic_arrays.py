from collections.abc import Sequence


class SingleArray(Sequence):
    """любая вставка/удаление всегда приводит к перевыделению всей занятой памяти"""
    def __init__(self, *args):
        self.list = [*args]

    def __getitem__(self, index: int):
        return self.list[index]

    def __len__(self) -> int:
        return len(self.list)

    #def resize(self, new_size):
    #    self.list = self.list[:new_size] + [None] * (len(self.list) - new_size)

    def insert(self, index: int, item) -> None:
        self.list = self.list[:index] + [item] + self.list[index:]

    def __delitem__(self, index):
        self.list = self.list[:index] + self.list[index + 1]

    def __str__(self):
        return str(self.list)


class VectorArray(Sequence):
    def __init__(self, *args):
        self.list = list(*args)

    def __getitem__(self, index: int):
        ...

    def __len__(self) -> int:
        ...

    def insert(self, index: int, item) -> None:
        ...

    def __delitem__(self, index):
        ...


class FactorArray(Sequence):
    def __init__(self, *args):
        self.list = list(*args)

    def __getitem__(self, index: int):
        ...

    def __len__(self) -> int:
        ...

    def insert(self, index: int, item) -> None:
        ...

    def __delitem__(self, index):
        ...


class MatrixArray(Sequence):
    def __init__(self, *args):
        self.list = list(*args)

    def __getitem__(self, index: int):
        ...

    def __len__(self) -> int:
        ...

    def insert(self, index: int, item) -> None:
        ...

    def __delitem__(self, index):
        ...
