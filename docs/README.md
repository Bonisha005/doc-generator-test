# Utils

A collection of utility functions for common data processing tasks.

## Overview

The `utils` module provides helper utilities, including functionality to format and export structured dictionary data as CSV text.

## API Reference

### `export_csv(data: list[dict], columns: list[str]) -> str`

Converts a list of dictionaries into CSV-formatted text using a specified column order.

#### Parameters

- **`data`** (`list[dict]`): A list of dictionaries representing the rows of data to export.
- **`columns`** (`list[str]`): A list of column header names determining the order and selection of fields included in the CSV output.

#### Returns

- **`str`**: A formatted CSV string containing headers followed by data rows.

## Usage Example

```python
from utils import export_csv

data = [
    {"id": 1, "name": "Alice", "role": "Developer"},
    {"id": 2, "name": "Bob", "role": "Designer"},
]

columns = ["id", "name", "role"]

csv_text = export_csv(data, columns)
print(csv_text)
```