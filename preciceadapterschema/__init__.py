"""
preCICE Adapter Schema Validation Package

This package provides validation functionality for preCICE adapter configurations.
"""

import json
from pathlib import Path

import jsonschema


# Cache for the loaded schema
_schema_cache = None


def validate(instance):
    """
    Validate instance data against the preCICE adapter configuration schema.
    
    Args:
        instance: The configuration data to validate (dict or JSON-compatible object)
    
    Raises:
        jsonschema.exceptions.ValidationError: If the instance is invalid
        jsonschema.exceptions.SchemaError: If the schema itself is invalid
    """
    global _schema_cache
    
    # Load the schema only once and cache it
    if _schema_cache is None:
        schema_path = Path(__file__).parent / "precice_adapter_config.schema.json"
        with open(schema_path, 'r') as schema_file:
            _schema_cache = json.load(schema_file)
    
    # Validate the instance against the cached schema
    jsonschema.validate(instance=instance, schema=_schema_cache)


__all__ = ['validate']
