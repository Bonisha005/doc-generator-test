# Utils

A Python utility module for common data formatting and export operations.

## Overview

This module provides helper functions for processing and exporting data structures, using Python's standard libraries (`csv`, `io`).

## API Reference

### `export_csv(data: list[dict], columns: list[str]) -> str`

Converts a list of dictionaries into a CSV-formatted string for a specified set of column keys.

#### Parameters

- **`data`** (`list[dict]`): A list of dictionaries where each dictionary represents a row of data.
- **`columns`** (`list[str]`): A list of keys to extract from each dictionary to include as CSV columns.

#### Returns

- **`str`**: A CSV-formatted string containing the header row followed by the corresponding data rows.

## Usage Example

```python
from utils import export_csv

data = [
    {"id": 1, "name": "Alice", "role": "Admin"},
    {"id": 2, "name": "Bob", "role": "User"},
]

columns = ["id", "name"]

csv_string = export_csv(data, columns)
print(csv_string)
```