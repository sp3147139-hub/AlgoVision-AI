def bubble_sort(values):
    arr = list(values)
    n = len(arr)
    comparisons = 0
    swaps = 0
    steps = []

    def record(action, comparing, sorted_from, message):
        steps.append({
            "action": action,
            "array": arr.copy(),
            "comparing": comparing,
            "sorted_from": sorted_from,  # indices >= this are final
            "message": message,
        })

    record("start", [], n, "Initial array.")

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            record("compare", [j, j + 1], n - i,
                   f"Compare {arr[j]} and {arr[j + 1]}.")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
                record("swap", [j, j + 1], n - i,
                       f"{arr[j + 1]} > {arr[j]}, so swap them.")
        if not swapped:
            record("early_exit", [], n - i,
                   "No swaps in this pass, so the array is already sorted.")
            break

    record("sorted", [], 0, "Array is sorted.")

    return {
        "steps": steps,
        "comparisons": comparisons,
        "swaps": swaps,
        "sorted_array": arr.copy(),
    }