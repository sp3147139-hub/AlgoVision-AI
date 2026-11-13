import random

import pytest

from algorithms.selection_sort import selection_sort


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([5], [5]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([5, 3, 3, 1], [1, 3, 3, 5]),
        ([10, -5, 0, 3], [-5, 0, 3, 10]),
    ],
)
def test_selection_sort(values, expected):
    result = selection_sort(values)
    steps = result["steps"]

    assert steps[0]["action"] == "start"
    assert steps[-1]["action"] == "sorted"
    assert steps[-1]["array"] == expected
    assert result["sorted_array"] == expected


def test_original_array_unchanged():
    original = [5, 3, 4, 1, 2]
    copy = original.copy()

    selection_sort(original)

    assert original == copy


def test_swap_count():
    result = selection_sort([4, 3, 2, 1])
    swap_steps = [s for s in result["steps"] if s["action"] == "swap"]

    assert result["swaps"] == 2
    assert len(swap_steps) == 2


def test_comparison_count():
    # n * (n - 1) / 2 comparisons for n = 5
    assert selection_sort([5, 4, 3, 2, 1])["comparisons"] == 10


def test_steps_have_keys_used_by_page():
    for step in selection_sort([3, 1, 2])["steps"]:
        for key in ("action", "array", "comparing", "minimum", "message"):
            assert key in step


def test_random_matches_sorted():
    for _ in range(100):
        data = [random.randint(-50, 50) for _ in range(random.randint(0, 20))]
        original = data.copy()

        result = selection_sort(data)

        assert result["sorted_array"] == sorted(original)
        assert data == original