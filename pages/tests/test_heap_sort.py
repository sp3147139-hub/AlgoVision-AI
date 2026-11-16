import random

import pytest

from algorithms.heap_sort import heap_sort


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
def test_heap_sort(values, expected):
    result = heap_sort(values)

    assert result["steps"][0]["action"] == "start"
    assert result["steps"][-1]["action"] == "sorted"
    assert result["sorted_array"] == expected


def test_original_unchanged():
    original = [5, 3, 4, 1, 2]
    copy = original.copy()
    heap_sort(original)
    assert original == copy


def test_steps_have_keys_used_by_page():
    for step in heap_sort([3, 1, 2])["steps"]:
        for key in ("action", "array", "comparing", "heap_size", "message"):
            assert key in step


def test_sorted_region_only_grows():
    sizes = [s["heap_size"] for s in heap_sort([9, 4, 7, 1, 8, 2])["steps"]]
    assert sizes == sorted(sizes, reverse=True)


def test_random_matches_sorted():
    for _ in range(100):
        data = [random.randint(-50, 50) for _ in range(random.randint(0, 20))]
        assert heap_sort(data)["sorted_array"] == sorted(data)