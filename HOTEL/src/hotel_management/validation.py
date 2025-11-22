class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


def is_valid_phone(phone: str) -> bool:
    """Check if phone number is exactly 10 digits."""
    if len(phone) != 10:
        return False
    return all(ch.isdigit() for ch in phone)


def parse_nights(nights_str: str) -> int:
    """
    Parse the nights input string and return a positive integer.

    Raises ValidationError if the input is empty, non-numeric, or < 1.
    """
    if not nights_str.strip():
        raise ValidationError("Please enter number of nights.")

    if not nights_str.isdigit():
        raise ValidationError("Nights must be a positive integer.")

    nights = int(nights_str)
    if nights < 1:
        raise ValidationError("Nights must be at least 1.")

    return nights
