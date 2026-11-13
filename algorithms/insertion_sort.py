def insertion_sort(values):
    arr = list(values)  # copy, input stays unchanged
    n = len(arr)
    comparisons = 0
    shifts = 0
    steps = []

    def record(action, comparing, key_index, sorted_upto, message):
        steps.append({
            "action": action,
            "array": arr.copy(),
            "comparing": comparing,
            "key_index": key_index,
            "sorted_upto": sorted_upto,  # last index of the sorted section
            "message": message,
        })

    record("start", [], None, 0 if n else -1,
           "Initial array. The first element is a sorted section of size 1.")

    for i in range(1, n):
        key = arr[i]
        pos = i
        record("select", [], pos, i - 1,
               f"Pick {key} (index {i}) as the key to insert into the sorted section.")

        while pos > 0:
            comparisons += 1
            record("compare", [pos - 1], pos, i - 1,
                   f"Compare {arr[pos - 1]} with key {key}.")

            if arr[pos - 1] > key:
                arr[pos] = arr[pos - 1]
                arr[pos - 1] = key
                pos -= 1
                shifts += 1
                record("shift", [pos + 1], pos, i - 1,
                       f"{arr[pos + 1]} > {key}, so shift {arr[pos + 1]} one step right.")
            else:
                break

        record("insert", [], None, i,
               f"Insert {key} at index {pos}. Sorted section now covers indices 0 to {i}.")

    record("sorted", [], None, n - 1, "Array is sorted.")

    return {
        "steps": steps,
        "comparisons": comparisons,
        "shifts": shifts,
        "sorted_array": arr.copy(),
    }