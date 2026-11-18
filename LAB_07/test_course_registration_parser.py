"""Property-based regression tests for the three registration parsers."""

import pytest
from hypothesis import given, settings, strategies as st

from course_registration_parser import (
    format_course_code,
    parse_student_record,
    total_credits,
)

ARBITRARY_INPUTS = st.text() | st.none()


@settings(max_examples=200)
@given(ARBITRARY_INPUTS)
def test_format_course_code_no_crash(value):
    try:
        result = format_course_code(value)
    except Exception as exc:
        pytest.fail(f"format_course_code crashed for {value!r}: {exc!r}")
    assert isinstance(result, str)


@settings(max_examples=200)
@given(ARBITRARY_INPUTS)
def test_total_credits_no_crash(value):
    try:
        result = total_credits(value)
    except Exception as exc:
        pytest.fail(f"total_credits crashed for {value!r}: {exc!r}")
    assert isinstance(result, int)
    assert result >= 0


@settings(max_examples=200)
@given(ARBITRARY_INPUTS)
def test_parse_student_record_no_crash(value):
    try:
        result = parse_student_record(value)
    except Exception as exc:
        pytest.fail(f"parse_student_record crashed for {value!r}: {exc!r}")
    assert set(result) == {"srn", "name", "status"}
    assert all(isinstance(part, str) for part in result.values())


def test_valid_examples_keep_expected_format():
    assert format_course_code("cs 301") == "CS301"
    assert total_credits("4, 3,4") == 11
    assert parse_student_record("pes1ug23cs001| Asha |REGULAR") == {
        "srn": "PES1UG23CS001",
        "name": "Asha",
        "status": "regular",
    }


def test_malformed_examples_are_safe():
    assert format_course_code(None) == ""
    assert format_course_code("cs") == ""
    assert total_credits("4,,nope,-2,3.5,2") == 6
    assert parse_student_record("only-srn") == {
        "srn": "ONLY-SRN",
        "name": "",
        "status": "",
    }
