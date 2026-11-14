def merge_sort(values):
    arr = list(values)
    n = len(arr)
    comparisons = 0
    writes = 0
    steps = []

    def record(action, comparing, active, message):
        steps.append({
            "action": action,
            "array": arr.copy(),
            "comparing": comparing,  # the slot being filled
            "range": active,         # [lo, hi] being worked on, or []
            "message": message,
        })

    def merge(lo, mid, hi):
        nonlocal comparisons, writes
        left = arr[lo:mid + 1]
        right = arr[mid + 1:hi + 1]
        i = j = 0
        k = lo
        record("merge_start", [], [lo, hi],
               f"Merge sorted halves {left} and {right}.")

        while i < len(left) and j < len(right):
            comparisons += 1
            record("compare", [k], [lo, hi],
                   f"Compare {left[i]} (left) with {right[j]} (right).")
            if left[i] <= right[j]:  # <= keeps the sort stable
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            writes += 1
            record("write", [k], [lo, hi], f"Place {arr[k]} at index {k}.")
            k += 1

        for rest in (left[i:], right[j:]):
            for value in rest:
                arr[k] = value
                writes += 1
                record("write", [k], [lo, hi],
                       f"Copy leftover {value} to index {k}.")
                k += 1

    def sort(lo, hi):
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        record("split", [], [lo, hi],
               f"Split indices {lo}..{hi} into {lo}..{mid} and {mid + 1}..{hi}.")
        sort(lo, mid)
        sort(mid + 1, hi)
        merge(lo, mid, hi)

    record("start", [], [], "Initial array.")
    sort(0, n - 1)
    record("sorted", [], [], "Array is sorted.")

    return {
        "steps": steps,
        "comparisons": comparisons,
        "writes": writes,
        "sorted_array": arr.copy(),
    }