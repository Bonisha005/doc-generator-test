"""
Small utility module for handling CSV exports, basic data validation,
list chunking, and dict merging.
"""
import csv
import moduke1

import io


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


def merge_dicts(base: dict, overrides: dict, deep: bool = False) -> dict:
    """
    Merges `overrides` into `base` and returns a new dict (does not mutate
    either input). By default this is a shallow merge -- overrides simply
    replace matching top-level keys. If `deep=True`, nested dict values are
    merged recursively instead of being replaced wholesale.

    Example:
        merge_dicts({"a": 1, "b": {"x": 1}}, {"b": {"y": 2}}, deep=True)
        -> {"a": 1, "b": {"x": 1, "y": 2}}

        merge_dicts({"a": 1, "b": {"x": 1}}, {"b": {"y": 2}}, deep=False)
        -> {"a": 1, "b": {"y": 2}}
    """
    result = dict(base)
    for key, value in overrides.items():
        if deep and isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = merge_dicts(result[key], value, deep=True)
        else:
            result[key] = value
    return result
