# Project

## Data Export

The `export_csv` function in `utils.py` converts a list of dictionaries into a CSV-formatted string.

### Usage

```python
from utils import export_csv

data = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
columns = ["name", "age"]

csv_output = export_csv(data, columns)
print(csv_output)
```