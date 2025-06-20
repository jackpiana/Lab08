from dataclasses import dataclass

@dataclass
class Nerc:
    _id: int
    _value: str

    @property
    def id(self):
        return self._id

    @property
    def value(self):
        return self._value

    def __str__(self):
        return f"{self._value} - {self._id}"

    def __hash__(self):
        return hash(self._id)


