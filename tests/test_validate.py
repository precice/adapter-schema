"""
Tests for the preciceadapterschema package.
"""

import unittest
import json

try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files

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

    def test_schema_file_accessible_via_importlib(self):
        """Test that the schema file is accessible via importlib.resources."""
        # Verify the schema can be loaded using importlib.resources
        try:
            schema_text = files("preciceadapterschema").joinpath("precice_adapter_config.schema.json").read_text()
            schema = json.loads(schema_text)
            self.assertIsInstance(schema, dict, "Schema should be a dictionary")
        except Exception as e:
            self.fail(f"Failed to load schema via importlib.resources: {e}")


if __name__ == '__main__':
    unittest.main()
