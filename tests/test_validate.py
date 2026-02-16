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
