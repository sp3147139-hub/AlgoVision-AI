import random

import pytest

from algorithms.quick_sort import quick_sort


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
def test_quick_sort(values, expected):
    result = quick_sort(values)

    assert result["steps"][0]["action"] == "start"
    assert result["steps"][-1]["action"] == "sorted"
    assert result["sorted_array"] == expected


def test_original_unchanged():
    original = [5, 3, 4, 1, 2]
    copy = original.copy()
    quick_sort(original)
    assert original == copy


def test_sorted_input_is_worst_case():
    # last-element pivot on sorted input: n(n-1)/2 comparisons, no swaps
    result = quick_sort([1, 2, 3, 4])
    assert result["comparisons"] == 6
    assert result["swaps"] == 0


def test_steps_have_keys_used_by_page():
    for step in quick_sort([3, 1, 2])["steps"]:
        for key in ("action", "array", "comparing", "pivot",
                    "range", "fixed", "message"):
            assert key in step


def test_random_matches_sorted():
    for _ in range(100):
        data = [random.randint(-50, 50) for _ in range(random.randint(0, 20))]
        result = quick_sort(data)
        assert result["sorted_array"] == sorted(data)
        n = len(data)
        assert result["comparisons"] <= n * (n - 1) // 2