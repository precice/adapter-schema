"""
preCICE Adapter Schema Validation Package

This package provides validation functionality for preCICE adapter configurations.
"""

import json

try:
    from importlib.resources import files
except ImportError:
    # Fallback for Python < 3.9
    from importlib_resources import files

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
        schema_text = files("preciceadapterschema").joinpath("precice_adapter_config.schema.json").read_text()
        _schema_cache = json.loads(schema_text)
    
    # Validate the instance against the cached schema
    jsonschema.validate(instance=instance, schema=_schema_cache)


__all__ = ['validate']
