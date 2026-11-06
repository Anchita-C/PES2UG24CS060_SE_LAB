import pytest

from course_registration import can_register, late_fee, waitlist_position


@pytest.mark.parametrize(
    ("student_status", "current_credits", "course_credits", "prerequisites_met", "expected"),
    [
        ("regular", 20, 4, True, "registered"),
        ("regular", 21, 4, True, "credit limit exceeded"),
        ("regular", 0, 3, False, "prerequisites missing"),
        ("probation", 12, 4, True, "registered"),
        ("honors", 24, 4, True, "registered"),
    ],
)
def test_can_register_decision_outcomes(
    student_status, current_credits, course_credits, prerequisites_met, expected
):
    assert (
        can_register(student_status, current_credits, course_credits, prerequisites_met)
        == expected
    )


@pytest.mark.parametrize(
    ("student_status", "course_credits", "message"),
    [
        ("unknown", 3, "unknown status"),
        ("regular", 0, "invalid course credits"),
        ("regular", -1, "invalid course credits"),
    ],
)
def test_can_register_validation_branches(student_status, course_credits, message):
    with pytest.raises(ValueError, match=message):
        can_register(student_status, 0, course_credits, True)


@pytest.mark.parametrize(
    ("enrolled", "capacity", "waitlist_length", "expected"),
    [
        (3, 4, 10, 0),
        (4, 4, 9, 10),
        (4, 4, 10, -1),
    ],
)
def test_waitlist_position_decision_outcomes(enrolled, capacity, waitlist_length, expected):
    assert waitlist_position(enrolled, capacity, waitlist_length) == expected


@pytest.mark.parametrize("capacity", [0, -1])
def test_waitlist_position_invalid_capacity_branch(capacity):
    with pytest.raises(ValueError, match="invalid capacity"):
        waitlist_position(4, capacity, 0)


@pytest.mark.parametrize(
    ("days_late", "credits", "has_waiver", "expected"),
    [
        (0, 21, False, 0),
        (1, 12, True, 0),
        (7, 20, False, 500),
        (8, 20, False, 600),
        (8, 21, False, 850),
        (25, 21, False, 2000),
    ],
)
def test_late_fee_decision_outcomes(days_late, credits, has_waiver, expected):
    assert late_fee(days_late, credits, has_waiver) == expected
