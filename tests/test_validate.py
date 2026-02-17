"""
Tests for the preciceadapterschema package.
"""

import unittest
import json
import os

try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files

import preciceadapterschema


class TestValidateFunction(unittest.TestCase):
    """Tests for the validate function."""

    def test_schema_file_accessible_via_importlib(self):
        """Test that the schema file is accessible via importlib.resources."""
        try:
            schema_text = files("preciceadapterschema").joinpath("precice_adapter_config.schema.json").read_text()
            schema = json.loads(schema_text)
            self.assertIsInstance(schema, dict, "Schema should be a dictionary")
        except Exception as e:
            self.fail(f"Failed to load schema via importlib.resources: {e}")


    def test_schema_for_valid_config(self):
        """Test that the validation function succeeds for a valid config."""
        valid_config_path = os.path.join(os.path.dirname(__file__), "configs", "valid_config.json")
        with open(valid_config_path, "r") as f:
            valid_config = json.load(f)
        try:
            preciceadapterschema.validate(valid_config)
        except Exception as e:
            self.fail(f"Validation failed for valid config: {e}")



    def test_schema_for_empty_config(self):
        """Test that the validation function fails for an empty config.
        As the schema requires certain fields, an empty config is invalid and should raise an exception."""
        empty_config_path = os.path.join(os.path.dirname(__file__), "configs", "empty_config.json")
        with open(empty_config_path, "r") as f:
            empty_config = json.load(f)
        try:
            preciceadapterschema.validate(empty_config)
            # If we reach this point, the validation did not raise an exception as expected
            self.fail("Validation did not fail for empty config as expected")
        except Exception as e:
            # We expect an exception, so this is a success case
            pass


    def test_schema_for_invalid_config(self):
        """Test that the validation function fails for a invalid config."""
        invalid_config_path = os.path.join(os.path.dirname(__file__), "configs", "invalid_config.json")
        with open(invalid_config_path, "r") as f:
            invalid_config = json.load(f)
        try:
            preciceadapterschema.validate(invalid_config)
            # If we reach this point, the validation did not raise an exception as expected
            self.fail("Validation did not fail for invalid config as expected")
        except Exception as e:
            # We expect an exception, so this is a success case
            pass




if __name__ == '__main__':
    unittest.main()
