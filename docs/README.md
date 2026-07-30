# Utils

A utility module providing helper functions for data manipulation and formatting.

## Functions

### `export_csv(data, columns)`

Converts a list of dictionaries into a CSV-formatted string using the specified column order.

#### Parameters

- **`data`** (`list[dict]`): A list of dictionaries where each dictionary represents a row of data.
- **`columns`** (`list[str]`): A list of column names specifying the keys to include and their order in the output CSV.

#### Returns

- **`str`**: A string containing the formatted CSV data with headers.

#### Usage Example

```python
from utils import export_csv

data = [
    {"id": 1, "name": "Alice", "role": "Admin"},
    {"id": 2, "name": "Bob", "role": "User"}
]

csv_output = export_csv(data, columns=["id", "name", "role"])
print(csv_output)
```