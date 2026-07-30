# Utils

A Python utility library providing helper functions for processing and exporting structured data.

## Features

- **CSV Export**: Convert lists of dictionaries into formatted CSV string output with custom column ordering.

## Usage

### Exporting Data to CSV

Use `export_csv` from `utils.py` to convert structured dictionary data into CSV text.

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

### API Reference

#### `export_csv(data: list[dict], columns: list[str]) -> str`

Converts a list of dictionaries into a CSV formatted string.

- **`data`**: A list of dictionaries where each dictionary represents a row of data.
- **`columns`**: A list of column header names specifying the order of fields in the exported CSV.
- **Returns**: A string containing the generated CSV data.