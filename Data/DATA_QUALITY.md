# Data Quality Notes

The sample data is synthetic and intentionally small.

Checks:
- Headers are present.
- IDs are unique within each table.
- Numeric fields follow consistent formats.
- No direct personal identifiers are included.
- Dates use YYYY-MM-DD.
- Difficulty values are 1–5.
- Scores and completion are percentages.

Before ML training:
- check duplicates
- analyze missing values
- inspect outliers
- inspect class balance
- check temporal leakage
- verify train/test separation
