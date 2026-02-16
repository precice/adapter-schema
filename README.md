# adapter-schema

Here the adapter configuration schema is stored, together with validation utility.

## Installation

Install the package using pip:

```bash
pip install preciceadapterschema
```

For development, install in editable mode:

```bash
pip install -e .
```

## Usage

The `preciceadapterschema` package provides a `validate` function to validate preCICE adapter configurations against the JSON schema.

```python
import preciceadapterschema

# Your configuration data
config_data = {
    "key": "value",
    "number": 42
}

# Validate the configuration
try:
    preciceadapterschema.validate(config_data)
    print("Configuration is valid!")
except Exception as e:
    print(f"Validation failed: {e}")
```

The schema file (`precice_adapter_config.schema.json`) is included in the package and loaded automatically by the `validate` function.

## Development

### Running Tests

Run tests using unittest:

```bash
python -m unittest discover -s tests -v
```

## License

This project is licensed under the LGPL-3.0 License - see the LICENSE file for details.
