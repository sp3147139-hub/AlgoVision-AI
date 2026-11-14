import random

import pytest

from algorithms.merge_sort import merge_sort


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
def test_merge_sort(values, expected):
    result = merge_sort(values)

    assert result["steps"][0]["action"] == "start"
    assert result["steps"][-1]["action"] == "sorted"
    assert result["sorted_array"] == expected


def test_original_unchanged():
    original = [5, 3, 4, 1, 2]
    copy = original.copy()
    merge_sort(original)
    assert original == copy


def test_counts_for_four_reversed():
    result = merge_sort([4, 3, 2, 1])
    assert result["comparisons"] == 4
    assert result["writes"] == 8  # n * log2(n) * ... = 4 per level x 2 levels


def test_steps_have_keys_used_by_page():
    for step in merge_sort([3, 1, 2])["steps"]:
        for key in ("action", "array", "comparing", "range", "message"):
            assert key in step


def test_random_matches_sorted():
    for _ in range(100):
        data = [random.randint(-50, 50) for _ in range(random.randint(0, 20))]
        assert merge_sort(data)["sorted_array"] == sorted(data)