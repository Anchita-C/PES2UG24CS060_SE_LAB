"""Robust parsers for course registration input."""


def format_course_code(code):
    """Format a two-part course code such as ``cs 301`` as ``CS301``.

    Malformed or non-string inputs return an empty string instead of raising.
    """
    try:
        parts = str(code).split()
    except Exception:
        return ""
    if len(parts) != 2 or not parts[0] or not parts[1]:
        return ""
    return parts[0].upper() + parts[1]


def total_credits(text):
    """Sum valid non-negative whole-number credits from comma-separated input.

    Empty, malformed, negative, and non-string values contribute zero.
    """
    try:
        items = str(text).split(",")
    except Exception:
        return 0
    total = 0
    for item in items:
        try:
            value = int(item.strip())
        except (TypeError, ValueError, OverflowError):
            continue
        if value >= 0:
            total += value
    return total


def parse_student_record(line):
    """Parse ``SRN|name|status``; missing fields become empty strings."""
    try:
        parts = str(line).split("|", 2)
    except Exception:
        parts = []
    parts = (parts + ["", "", ""])[:3]
    try:
        srn = parts[0].strip().upper()
        name = parts[1].strip()
        status = parts[2].strip().lower()
    except Exception:
        return {"srn": "", "name": "", "status": ""}
    return {"srn": srn, "name": name, "status": status}


def main():
    print("==== Running format_course_code ====")
    value = input("Enter a course code as DEPT NUMBER (e.g. cs 301): ")
    print("Formatted course code:", format_course_code(value))

    print("\n==== Running total_credits ====")
    value = input("Enter course credits separated by commas (e.g. 4,3,4): ")
    print("Total credits:", total_credits(value))

    print("\n==== Running parse_student_record ====")
    value = input("Enter a student record as SRN|name|status (e.g. pes1ug23cs001|Asha|regular): ")
    print("Student record:", parse_student_record(value))


if __name__ == "__main__":
    main()
