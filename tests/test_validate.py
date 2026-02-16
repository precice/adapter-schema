"""
Tests for the preciceadapterschema package.
"""

import unittest
import json
from pathlib import Path

import preciceadapterschema


class TestValidateFunction(unittest.TestCase):
    """Tests for the validate function."""

    def test_validate_with_empty_schema(self):
        """Test that validation works with the empty schema."""
        # The empty schema should accept any valid JSON data
        test_data = {'key': 'value', 'number': 42}
        
        # Should not raise any exception
        try:
            preciceadapterschema.validate(test_data)
        except Exception as e:
            self.fail(f"Validation raised an unexpected exception: {e}")

    def test_validate_empty_dict(self):
        """Test validation with an empty dictionary."""
        try:
            preciceadapterschema.validate({})
        except Exception as e:
            self.fail(f"Validation raised an unexpected exception: {e}")

    def test_validate_list(self):
        """Test validation with a list."""
        try:
            preciceadapterschema.validate([1, 2, 3])
        except Exception as e:
            self.fail(f"Validation raised an unexpected exception: {e}")

    def test_validate_nested_structure(self):
        """Test validation with a nested structure."""
        test_data = {
            'config': {
                'nested': {
                    'value': 123
                },
                'list': [1, 2, 3]
            }
        }
        try:
            preciceadapterschema.validate(test_data)
        except Exception as e:
            self.fail(f"Validation raised an unexpected exception: {e}")

    def test_schema_file_exists(self):
        """Test that the schema file exists and is readable."""
        schema_path = Path(preciceadapterschema.__file__).parent / 'precice_adapter_config.schema.json'
        self.assertTrue(schema_path.exists(), "Schema file does not exist")
        
        # Verify it's valid JSON
        with open(schema_path, 'r') as f:
            schema = json.load(f)
            self.assertIsInstance(schema, dict, "Schema should be a dictionary")


if __name__ == '__main__':
    unittest.main()
