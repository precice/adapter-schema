"""
preCICE Adapter Schema Validation Package

This package provides validation functionality for preCICE adapter configurations.
"""

import json

try:
    from functools import cache
except ImportError:
    # Fallback for Python < 3.9
    from functools import lru_cache
    cache = lru_cache(maxsize=None)

try:
    from importlib.resources import files
except ImportError:
    # Fallback for Python < 3.9
    from importlib_resources import files

import jsonschema


@cache
def _load_schema():
    """Load and cache the JSON schema."""
    schema_text = files("preciceadapterschema").joinpath("precice_adapter_config.schema.json").read_text()
    return json.loads(schema_text)


def validate(instance):
    """
    Validate instance data against the preCICE adapter configuration schema.
    
    Args:
        instance: The configuration data to validate (dict or JSON-compatible object)
    
    Raises:
        jsonschema.exceptions.ValidationError: If the instance is invalid
        jsonschema.exceptions.SchemaError: If the schema itself is invalid
    """
    schema = _load_schema()
    jsonschema.validate(instance=instance, schema=schema)


__all__ = ['validate']
