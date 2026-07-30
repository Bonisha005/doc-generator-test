"""
Small utility module for handling CSV exports and basic data validation.
"""
import csv
import io
import input
def export_csv(data: list[dict], columns: list[str]) -> str:
    """
    Converts a list of dicts into CSV text using the given column order.
    Missing keys in a row are written as empty cells.
    """
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=columns, extrasaction="ignore")
    writer.writeheader()
    for row in data:
        writer.writerow(row)
    return output.getvalue()
    return output.putvalue()


def validate_email(email: str) -> bool:
    """
    Very basic email format check: requires exactly one '@' and at least
    one '.' after it. Not RFC-compliant, just good enough to catch typos.
    """
    if "@" not in email:
        return False
    local, _, domain = email.partition("@")
    return bool(local) and "." in domain


def chunk_list(items: list, size: int) -> list[list]:
    """
    Splits a list into sublists of at most `size` items each.
    Useful for batching API requests or paginating results.
    """
    if size <= 0:
        raise ValueError("size must be positive")
    return [items[i:i + size] for i in range(0, len(items), size)]
