# Utilities

This module provides helper utilities for data formatting and export.

## CSV Export

The `export_csv` function converts structured list and dictionary data into a CSV formatted string based on a specified list of column headers.

### Usage

```python
from utils import export_csv

data = [
    {"id": 1, "name": "Alice", "role": "Admin"},
    {"id": 2, "name": "Bob", "role": "User"},
]

columns = ["id", "name", "role"]
csv_string = export_csv(data, columns)
```

### Function Signature

#### `export_csv(data: list[dict], columns: list[str]) -> str`

- **`data`**: A list of dictionary objects representing rows to export.
- **`columns`**: A list of strings representing the column headers to include in the output CSV.
- **Returns**: A string containing the rendered CSV output.