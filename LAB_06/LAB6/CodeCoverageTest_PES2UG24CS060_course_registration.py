import pytest

from course_registration import can_register, late_fee, waitlist_position


@pytest.mark.parametrize(
    ("student_status", "current_credits", "course_credits", "expected"),
    [
        ("regular", 20, 4, "registered"),
        ("probation", 12, 4, "registered"),
        ("honors", 24, 4, "registered"),
        ("regular", 20, 5, "credit limit exceeded"),
        ("probation", 14, 3, "credit limit exceeded"),
        ("honors", 25, 4, "credit limit exceeded"),
    ],
)
def test_can_register_valid_statuses(student_status, current_credits, course_credits, expected):
    assert can_register(student_status, current_credits, course_credits, True) == expected


def test_can_register_rejects_unknown_status():
    with pytest.raises(ValueError, match="unknown status"):
        can_register("visitor", 0, 3, True)


@pytest.mark.parametrize("course_credits", [0, -1])
def test_can_register_rejects_nonpositive_course_credits(course_credits):
    with pytest.raises(ValueError, match="invalid course credits"):
        can_register("regular", 0, course_credits, True)


def test_can_register_requires_prerequisites():
    assert can_register("regular", 0, 3, False) == "prerequisites missing"


@pytest.mark.parametrize(
    ("enrolled", "capacity", "waitlist_length", "expected"),
    [
        (3, 4, 0, 0),
        (4, 4, 0, 1),
        (4, 4, 9, 10),
        (4, 4, 10, -1),
        (8, 4, 12, -1),
    ],
)
def test_waitlist_position(enrolled, capacity, waitlist_length, expected):
    assert waitlist_position(enrolled, capacity, waitlist_length) == expected


@pytest.mark.parametrize("capacity", [0, -1])
def test_waitlist_position_rejects_nonpositive_capacity(capacity):
    with pytest.raises(ValueError, match="invalid capacity"):
        waitlist_position(0, capacity, 0)


@pytest.mark.parametrize(
    ("days_late", "credits", "has_waiver", "expected"),
    [
        (0, 12, False, 0),
        (-1, 12, False, 0),
        (1, 12, True, 0),
        (1, 12, False, 500),
        (7, 12, False, 500),
        (8, 12, False, 600),
        (1, 21, False, 750),
        (23, 21, False, 2000),
        (30, 21, False, 2000),
    ],
)
def test_late_fee(days_late, credits, has_waiver, expected):
    assert late_fee(days_late, credits, has_waiver) == expected
