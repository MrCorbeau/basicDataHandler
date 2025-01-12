# Data Handler Package

## Description
The Data Handler Package is designed to simplify data handling tasks, particularly focused on CSV files. It provides various classes and methods to streamline common data operations.

## Installation
You can install the package using pip:
```bash
pip install DataHandlerForCSV
```

## Usage

--Missing Value Handler

```python
from program.missing_value_handler import HandleMissingValue as hmv

df = pd.DataFrame({"numbs" : [1, 2, None, 4]})
copy1 = df.copy()
df = hmv.fill_as_mean(copy1, "numbs")

copy2 = df.copy()
df = hmv.fill_as_median(copy2, "numbs")

copy3 = df.copy()
df = hmv.fill_as_constant(copy3, "numbs")

copy4 = df.copy()
df = hmv.drop(copy4, "numbs")
```
