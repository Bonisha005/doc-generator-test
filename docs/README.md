# Utils Module

The `utils` module provides a collection of helper functions for handling common data manipulation tasks, including CSV exporting, email validation, list chunking, and dictionary merging.

## Functions

### `export_csv(data: list[dict], columns: list[str]) -> str`
Converts a list of dictionaries into a CSV-formatted string using the specified column order. Any missing keys in individual rows are automatically written as empty cells.

### `validate_email(email: str) -> bool`
Validates whether the provided string is a properly formatted email address.

### `chunk_list(items: list, size: int) -> list[list]`
Splits a list into smaller chunks of a specified maximum size. Raises a `ValueError` if the size is not a positive integer.

### `merge_dicts(base: dict, overrides: dict, deep: bool = False) -> dict`
Merges an `overrides` dictionary into a `base` dictionary and returns a new dictionary without mutating either input. 

By default (`deep=False`), this performs a shallow merge where matching top-level keys in `overrides` completely replace those in `base`. When `deep=True`, nested dictionaries are merged recursively rather than being replaced wholesale.

Example:
```python
base = {"a": 1, "b": {"x": 1}}
overrides = {"b": {"y": 2}}

# Shallow merge (default)
merge_dicts(base, overrides, deep=False)
# Returns: {"a": 1, "b": {"y": 2}}

# Deep merge
merge_dicts(base, overrides, deep=True)
# Returns: {"a": 1, "b": {"x": 1, "y": 2}}
```