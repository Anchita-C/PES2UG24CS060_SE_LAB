# LAB 07 - Fuzz Testing for Input Validation Bugs

This folder contains the independent Lab 7 implementation for the course registration parser. The upstream course repository remains unchanged.

## Files

- `course_registration_parser.py` - defensive implementations of all three parser functions.
- `test_course_registration_parser.py` - Hypothesis tests that generate arbitrary text and `None` values, plus fixed valid and malformed examples.
- `requirements.txt` - test dependencies.
- `PES2UG24CS060_AnchitaChhibba_LAB7.pdf` - console output records and reflection notes.

## Run

```sh
python -m pip install -r requirements.txt
python course_registration_parser.py
python -m pytest -q test_course_registration_parser.py
```

The interactive program asks for a course code, a comma-separated credit list, and a student record. Functions return safe defaults for malformed input: an empty string for an invalid course code, zero for credits, and a dictionary with empty fields for an incomplete student record.

## What fuzzing found

The original code assumed a string with a fixed number of fields, so `None`, missing tokens, empty comma-separated elements, and nonnumeric credit strings could raise `AttributeError`, `ValueError`, or `IndexError`. The replacement tests use Hypothesis to explore arbitrary strings and `None`; the repaired functions keep their return types stable and do not leak those parsing exceptions.

The attached handout contains no explicit reflection questions, although the course repository README requests three reflection answers. The PDF therefore answers three lab-aligned reflection prompts and identifies them as such.
