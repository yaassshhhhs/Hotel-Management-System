import unittest

from src.hotel_management.validation import is_valid_phone, parse_nights, ValidationError


class TestValidation(unittest.TestCase):

    def test_valid_phone(self):
        self.assertTrue(is_valid_phone("9876543210"))

    def test_invalid_phone_length(self):
        self.assertFalse(is_valid_phone("12345"))

    def test_invalid_phone_characters(self):
        self.assertFalse(is_valid_phone("98765abc10"))

    def test_parse_nights_valid(self):
        self.assertEqual(parse_nights("3"), 3)

    def test_parse_nights_empty(self):
        with self.assertRaises(ValidationError):
            parse_nights("")

    def test_parse_nights_non_numeric(self):
        with self.assertRaises(ValidationError):
            parse_nights("three")

    def test_parse_nights_less_than_one(self):
        with self.assertRaises(ValidationError):
            parse_nights("0")


if __name__ == "__main__":
    unittest.main()
