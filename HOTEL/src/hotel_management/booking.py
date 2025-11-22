from datetime import date, timedelta
from .models import Guest
from . import storage
from .validation import is_valid_phone, parse_nights, ValidationError


class BookingError(Exception):
    """Custom exception for booking-related errors."""
    pass


def book_guest(name: str, phone: str, room_type: str, nights_str: str) -> Guest:
    """
    Book a guest into the hotel.

    Validates inputs, checks room availability, updates storage, and
    returns the created Guest instance.

    Raises BookingError or ValidationError on failures.
    """
    name = name.strip()
    phone = phone.strip()

    if not name:
        raise BookingError("Name is required.")

    if not is_valid_phone(phone):
        raise BookingError("Phone number must be exactly 10 digits, digits only.")

    nights = parse_nights(nights_str)

    # Check room availability
    if storage.get_available_rooms(room_type) <= 0:
        raise BookingError(f"No vacant {room_type} rooms!")

    check_in = date.today()
    check_out = check_in + timedelta(days=nights)

    guest = Guest(
        name=name,
        phone=phone,
        room_type=room_type,
        nights=nights,
        check_in=check_in,
        check_out=check_out,
    )

    # Update storage
    storage.allocate_room(room_type)
    storage.add_guest(guest)

    return guest


def checkout_guest(index: int) -> Guest:
    """
    Checkout a guest by index.

    Removes the guest from storage and releases the room.
    Returns the removed Guest instance.
    """
    guest = storage.remove_guest(index)
    storage.release_room(guest.room_type)
    return guest
