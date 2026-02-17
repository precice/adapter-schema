# preCICE Adapter Schema

Here the adapter configuration schema is stored, together with validation utility.

A schema ...

- defines how a configuration file looks like (thus replaces any explicit documentation).
- enables interoperability (through standardization).
- simplifies auto-generation.
- enables tooling support (e.g. IDEs or GUIs).
- enables automatic LLM-based conversion from and to other configuration languages.
- ...

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
}

# Validate the configuration
try:
    preciceadapterschema.validate(config_data)
    print("Configuration is valid!")
except Exception as e:
    print(f"Validation failed: {e}")
```

The schema file (`precice_adapter_config.schema.json`) is included in the package and loaded automatically by the `validate` function.

## Configuring preCICE Adapters

We recommend using [MetaConfigurator](https://metaconfigurator.org/?schema=https://github.com/precice/adapter-schema/blob/main/preciceadapterschema/precice_adapter_config.schema.json&settings=https://github.com/precice/adapter-schema/blob/main/metaconfigurator_settings.json) to create and edit preCICE adapter configurations. It provides a user-friendly interface and ensures that your configurations are always valid according to the schema.

## Development

### Running Tests

Run tests using unittest:

```bash
python -m unittest discover -s tests -v
```
