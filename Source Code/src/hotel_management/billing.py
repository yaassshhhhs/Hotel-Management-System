from .models import Guest, ROOM_RATES


def calculate_bill(guest: Guest) -> int:
    """Calculate total bill for a guest based on room type and nights."""
    rate = ROOM_RATES.get(guest.room_type, 0)
    return guest.nights * rate


def format_bill_text(guest: Guest) -> str:
    """Return a formatted bill string suitable for display in the GUI."""
    rate = ROOM_RATES.get(guest.room_type, 0)
    total = calculate_bill(guest)
    return (
        f"Bill for {guest.name} - Room: {guest.room_type}\n"
        f"Nights: {guest.nights} x ₹{rate} = ₹{total}"
    )
