import unittest
import contact_manager


class TestContactManager(unittest.TestCase):

    def setUp(self):
        """Clear the contacts before each test."""
        contact_manager.contacts.clear()

    def test_add_contact(self):
        """Test adding a new contact."""
        contact_manager.add_contact("John", "555-1234")
        self.assertEqual(
            contact_manager.contacts["John"], "555-1234"
        )

    def test_find_existing_contact(self):
        """Test finding an existing contact."""
        contact_manager.add_contact("John", "555-1234")

        result = contact_manager.find_contact("John")

        self.assertEqual(result, "555-1234")

    def test_find_nonexistent_contact(self):
        """Test finding a missing contact."""
        result = contact_manager.find_contact("Jane")

        self.assertIsNone(result)

    def test_delete_existing_contact(self):
        """Test deleting an existing contact."""
        contact_manager.add_contact("John", "555-1234")

        contact_manager.delete_contact("John")

        self.assertNotIn("John", contact_manager.contacts)

    def test_delete_nonexistent_contact(self):
        """Test deleting a missing contact."""
        contact_manager.delete_contact("Jane")

        self.assertNotIn("Jane", contact_manager.contacts)

    def test_duplicate_contact(self):
        """Test that duplicate contacts are not allowed."""
        contact_manager.add_contact("John", "555-1234")

        with self.assertRaises(contact_manager.DuplicateContactError):
            contact_manager.add_contact("John", "555-5678")

        self.assertEqual(
            contact_manager.contacts["John"], "555-1234"
        )


if __name__ == "__main__":
    unittest.main()