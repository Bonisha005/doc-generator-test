# Utilities

A utility module providing helper functions for exporting data to CSV format.

## Overview

The `utils.py` module provides functions for handling CSV operations and formatting data for export.

## API Reference

### `export_csv(data, columns)`

Converts a list of dictionaries into a formatted CSV string.

#### Parameters

* **`data`** (`list[dict]`): A list of dictionaries representing rows of data, where keys map to column names.
* **`columns`** (`list[str]`): A list of column header strings specifying which keys to include and their order in the CSV output.

#### Returns

* **`str`**: A string containing the formatted CSV content.

## Usage Example

```python
from utils import export_csv

data = [
    {"name": "Alice", "role": "Engineer"},
    {"name": "Bob", "role": "Designer"}
]
columns = ["name", "role"]

csv_output = export_csv(data, columns)
print(csv_output)
```