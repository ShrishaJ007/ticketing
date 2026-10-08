from dataclasses import dataclass

@dataclass
class Event:
    name: str
    date: str
    total_tickets: int
    price: float