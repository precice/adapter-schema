"""
preCICE Adapter Schema Validation Package

This package provides validation functionality for preCICE adapter configurations.
"""

import json
from pathlib import Path

import jsonschema


def validate(instance):
    """
    Validate instance data against the preCICE adapter configuration schema.
    
    Args:
        instance: The configuration data to validate (dict or JSON-compatible object)
    
    Raises:
        jsonschema.exceptions.ValidationError: If the instance is invalid
        jsonschema.exceptions.SchemaError: If the schema itself is invalid
    """
    # Get the path to the schema file in this package
    schema_path = Path(__file__).parent / "precice_adapter_config.schema.json"
    
    # Load the schema
    with open(schema_path, 'r') as schema_file:
        schema = json.load(schema_file)
    
    # Validate the instance against the schema
    jsonschema.validate(instance=instance, schema=schema)


__all__ = ['validate']
