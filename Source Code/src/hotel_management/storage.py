from typing import List, Dict
from .models import Guest, DEFAULT_ROOM_COUNTS

# In-memory storage for guests and room inventory

_guests: List[Guest] = []
_rooms: Dict[str, int] = DEFAULT_ROOM_COUNTS.copy()


def get_guests() -> List[Guest]:
    """Return a copy of the current guest list."""
    return list(_guests)


def add_guest(guest: Guest) -> None:
    """Add a guest booking to the in-memory list."""
    _guests.append(guest)


def remove_guest(index: int) -> Guest:
    """
    Remove a guest by index and return it.
    Raises IndexError if index is invalid.
    """
    guest = _guests.pop(index)
    return guest


def get_available_rooms(room_type: str) -> int:
    """Get available room count for a given room type."""
    return _rooms.get(room_type, 0)


def allocate_room(room_type: str) -> None:
    """Decrease room count when a room is booked."""
    if _rooms[room_type] <= 0:
        raise ValueError(f"No vacant {room_type} rooms available.")
    _rooms[room_type] -= 1


def release_room(room_type: str) -> None:
    """Increase room count when a room is released on checkout."""
    _rooms[room_type] += 1
