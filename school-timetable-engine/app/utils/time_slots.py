from typing import List, Tuple

# Default working days for a school week
DAYS: List[str] = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]

# Period numbers per day (can be adjusted per school)
PERIODS: List[int] = [1, 2, 3, 4, 5, 6, 7]


def all_time_slots() -> List[Tuple[str, int]]:
    """
    Returns all possible (day, period) combinations.
    Example: [("Monday", 1), ("Monday", 2), ...]
    """
    return [(day, period) for day in DAYS for period in PERIODS]
