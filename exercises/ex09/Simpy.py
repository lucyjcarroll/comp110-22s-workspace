"""Utility class for numerical operations."""

from __future__ import annotations
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
        """Creates ability to use + in conjunction with Simpy objects and floats."""
        new: Simpy = Simpy([]) 
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(rhs.values)):
                new.values.append(self.values[item] + rhs.values[item])
        if isinstance(rhs, float):
            for item in range(len(self.values)):
                new.values.append(self.values[item] + rhs)
        return new

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Creates ability to exponentiate 2 Simpy objects or a Simpy object and a float."""
        new: Simpy = Simpy([]) 
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(rhs.values)):
                new.values.append(self.values[item] ** rhs.values[item])
        if isinstance(rhs, float):
            for item in range(len(self.values)):
                new.values.append(self.values[item] ** rhs)
        return new

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Creates a list of True or False assertions based on whether or not Simpy values or float values match the original Simpy values."""
        mask: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(rhs.values)):
                if self.values[i] == rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
        if isinstance(rhs, float):
            for item in range(len(self.values)):
                if self.values[item] == rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        return mask

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Creates a list of True or False assertions based on whether Simpy values or float values are greater than the original Simpy values."""
        mask: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(rhs.values)):
                if self.values[i] > rhs.values[i]:
                    mask.append(True)
                else:
                    mask.append(False)
        if isinstance(rhs, float):
            for item in range(len(self.values)):
                if self.values[item] > rhs:
                    mask.append(True)
                else:
                    mask.append(False)
        return mask

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Produces ability to return a list only including masked (filtered) items."""
        new: Simpy = Simpy([])
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(rhs) == len(self.values)
            i: int = 0
            while i < len(rhs):
                if rhs[i]:
                    new.values.append(self.values[i])
                i = i + 1
        return new