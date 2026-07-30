# Utils

A Python utility module providing helper functions for data conversion and export operations.

## Features

- **CSV Export**: Convert lists of dictionaries into formatted CSV text strings with defined column ordering.

## Usage

### `export_csv`

Converts a list of dictionaries into a CSV-formatted string using the specified column order.

```python
from utils import export_csv

data = [
    {"id": 1, "name": "Alice", "role": "Admin"},
    {"id": 2, "name": "Bob"},  # Missing keys will be rendered as empty cells
]

columns = ["id", "name", "role"]

csv_output = export_csv(data, columns)
print(csv_output)
```

#### Parameters

- **`data`** (`list[dict]`): A list of dictionaries where each dictionary represents a row of data.
- **`columns`** (`list[str]`): A list of column names defining the order of fields in the CSV output.

#### Returns

- **`str`**: A CSV formatted string including the header row.

#### Behavior

- **Missing Keys**: If a dictionary in `data` lacks a key defined in `columns`, the cell is left blank.
- **Extra Keys**: Keys present in `data` dictionaries that are not listed in `columns` are ignored.