from dataclasses import dataclass


@dataclass
class Event:
    name: str
    date: str
    total_tickets: int
    price: float


def double(x: int) -> int:
    return x * 2
