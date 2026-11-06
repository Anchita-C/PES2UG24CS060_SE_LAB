# Course Registration

Lab 6: Code and Branch Coverage

## About

A small Python module that decides whether a student can register for a course, works out waitlist positions and charges late registration fees.

## Files

| File | Description |
|------|-------------|
| `course_registration.py` | The module under test |
| `test_course_registration.py` | Starter test file |
| `CodeCoverageTest_PES2UG24CS060_course_registration.py` | Code coverage tests |
| `BranchCoverageTest_PES2UG24CS060_course_registration.py` | Branch coverage tests |

## Run the tests

From this directory, run each coverage suite independently:

```sh
python3 -m pytest -q CodeCoverageTest_PES2UG24CS060_course_registration.py
python3 -m pytest -q BranchCoverageTest_PES2UG24CS060_course_registration.py
```

To measure statement and branch coverage for either suite:

```sh
python3 -m coverage run --branch --source=course_registration -m pytest -q CodeCoverageTest_PES2UG24CS060_course_registration.py
python3 -m coverage report
```

Replace the code coverage test filename with the branch coverage test filename to measure that suite instead.
