# Utils

Utility module providing helper functions for data processing and export operations.

## Features

### CSV Export

The `utils` module includes functionality for converting structured dictionary data into CSV formatted text.

```python
from utils import export_csv

data = [
    {"name": "Alice", "role": "Engineer"},
    {"name": "Bob", "role": "Designer"}
]
columns = ["name", "role"]

csv_output = export_csv(data, columns)
```

#### Functions

##### `export_csv(data: list[dict], columns: list[str]) -> str`
Converts a list of dictionaries into a CSV-formatted string based on the provided column order.

- **`data`**: A list of dictionaries where keys represent column names and values represent row entries.
- **`columns`**: A list of strings defining the column header order in the generated CSV output.
- **Returns**: A string containing the formatted CSV data.