import random

import pytest

from algorithms.insertion_sort import insertion_sort


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([5], [5]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([5, 3, 3, 1], [1, 3, 3, 5]),
        ([10, -5, 0, 3], [-5, 0, 3, 10]),
        ([8, 7, 6, 5, 4], [4, 5, 6, 7, 8]),
    ],
)
def test_insertion_sort(values, expected):
    result = insertion_sort(values)
    steps = result["steps"]

    assert steps[0]["action"] == "start"
    assert steps[-1]["action"] == "sorted"
    assert steps[-1]["array"] == expected
    assert result["sorted_array"] == expected


def test_original_array_unchanged():
    original = [5, 3, 4, 1, 2]
    copy = original.copy()

    insertion_sort(original)

    assert original == copy


def test_records_shifts():
    result = insertion_sort([4, 3, 2, 1])
    shift_steps = [s for s in result["steps"] if s["action"] == "shift"]

    assert result["shifts"] == 6
    assert len(shift_steps) == 6


def test_records_insertions():
    steps = insertion_sort([4, 3, 2, 1])["steps"]
    insertions = [s for s in steps if s["action"] == "insert"]

    assert len(insertions) == 3


def test_best_case_comparisons():
    # sorted input: n - 1 comparisons, 0 shifts
    result = insertion_sort([1, 2, 3, 4, 5])

    assert result["comparisons"] == 4
    assert result["shifts"] == 0


def test_worst_case_comparisons():
    # reversed input: n(n-1)/2 comparisons and shifts
    result = insertion_sort([5, 4, 3, 2, 1])

    assert result["comparisons"] == 10
    assert result["shifts"] == 10


def test_steps_have_keys_used_by_page():
    for step in insertion_sort([3, 1, 2])["steps"]:
        for key in ("action", "array", "comparing", "key_index",
                    "sorted_upto", "message"):
            assert key in step


def test_random_matches_sorted():
    for _ in range(100):
        data = [random.randint(-50, 50) for _ in range(random.randint(0, 20))]
        original = data.copy()

        result = insertion_sort(data)

        assert result["sorted_array"] == sorted(original)
        assert data == original