from dataclasses import dataclass
from datetime import date
from typing import Dict

@dataclass
class Guest:
    """Represents a guest booking in the hotel."""
    name: str
    phone: str
    room_type: str
    nights: int
    check_in: date
    check_out: date


# Supported room types
ROOM_TYPES = ("Single", "Double", "Suite")

# Initial number of rooms for each type
DEFAULT_ROOM_COUNTS: Dict[str, int] = {
    "Single": 5,
    "Double": 3,
    "Suite": 2,
}

# Per-night room rates
ROOM_RATES: Dict[str, int] = {
    "Single": 800,
    "Double": 1200,
    "Suite": 2000,
}
