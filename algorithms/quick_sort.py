def quick_sort(values):
    arr = list(values)
    n = len(arr)
    comparisons = 0
    swaps = 0
    steps = []
    fixed = set()  # indices already in their final position

    def record(action, comparing, pivot, active, message):
        steps.append({
            "action": action,
            "array": arr.copy(),
            "comparing": comparing,
            "pivot": pivot,        # pivot index, or None
            "range": active,       # [lo, hi] being partitioned, or []
            "fixed": sorted(fixed),
            "message": message,
        })

    def partition(lo, hi):
        nonlocal comparisons, swaps
        pivot = arr[hi]
        i = lo - 1
        record("pivot", [], hi, [lo, hi],
               f"Pick {pivot} (last element) as the pivot for indices {lo}..{hi}.")

        for j in range(lo, hi):
            comparisons += 1
            record("compare", [j], hi, [lo, hi],
                   f"Is {arr[j]} < pivot {pivot}?")
            if arr[j] < pivot:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
                    record("swap", [i, j], hi, [lo, hi],
                           f"Yes: swap indices {i} and {j} to move the small value left.")

        p = i + 1
        if p != hi:
            arr[p], arr[hi] = arr[hi], arr[p]
            swaps += 1
        fixed.add(p)
        record("place", [], p, [lo, hi],
               f"Place pivot {pivot} at index {p}. It is now in its final position.")
        return p

    def sort(lo, hi):
        if lo > hi:
            return
        if lo == hi:
            fixed.add(lo)
            record("single", [], None, [lo, hi],
                   f"Index {lo} has one element, so it is already final.")
            return
        p = partition(lo, hi)
        sort(lo, p - 1)
        sort(p + 1, hi)

    record("start", [], None, [], "Initial array.")
    sort(0, n - 1)
    fixed.update(range(n))
    record("sorted", [], None, [], "Array is sorted.")

    return {
        "steps": steps,
        "comparisons": comparisons,
        "swaps": swaps,
        "sorted_array": arr.copy(),
    }