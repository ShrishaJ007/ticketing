from ticketing.models import Event


def main() -> None:
    event = Event(
        name="College Fest", date="2026-11-15", total_tickets=500, price=299.0
    )
    print(event)
    print(f"{event.name} has {event.total_tickets} tickets at Rs {event.price} each")
