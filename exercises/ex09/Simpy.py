"""Utility class for numerical operations."""

from __future__ import annotations
from re import L
from typing import Union

__author__ = "730320310"


class Simpy:
    """A new class that takes a list of values."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Initializing values to Simpy object."""
        self.values = values

    def add_on(self, add_on: str) -> list[float]:
        """Constructor to add '0' to values in a list."""
        for i in self.values:
            self.values[i] = self.values[i] + "0"

    def __str__(self) -> str:
        """Produce a str representation of the values list."""
        return f"Simpy({self.values})"

    def fill(self, float_val: float, num_val: int) -> None:
        """Mutates list to produce a new list with a new float value and new number of values."""
        self.values: list[float] = []
        for item in range(0, num_val):
            self.values.append(float_val)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None: 
        """Produces a list with a range of values (floats)."""
        assert step != 0.0
        item: float = start
        while abs(item) < abs(stop):
            self.values.append(item)
            item += step

    def sum(self) -> float:
        """Returns sum of all items in values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Creates ability to use + in conjunction with  Simpy objects and floats."""
        new: Simpy 
        if isinstance(rhs, Simpy):
            len(self.values) == len(Simpy.values)
            for item in self.values:
                new = self.values(item) + Simpy.values(item)
        if isinstance(rhs, float):
            

    # def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:

    # def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:

    # def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:

    # def __getitem__(self, rhs: int) -> float:
    #     value: float
    #     self.values[value]
    #     return value



