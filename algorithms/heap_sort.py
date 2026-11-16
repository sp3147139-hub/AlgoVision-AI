def heap_sort(values):
    arr = list(values)
    n = len(arr)
    comparisons = 0
    swaps = 0
    steps = []

    def record(action, comparing, heap_size, message):
        steps.append({
            "action": action,
            "array": arr.copy(),
            "comparing": comparing,
            "heap_size": heap_size,  # indices >= heap_size are sorted
            "message": message,
        })

    def heapify(size, root):
        nonlocal comparisons, swaps
        while True:
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2

            if left < size:
                comparisons += 1
                record("compare", [largest, left], size,
                       f"Compare parent {arr[largest]} with left child {arr[left]}.")
                if arr[left] > arr[largest]:
                    largest = left

            if right < size:
                comparisons += 1
                record("compare", [largest, right], size,
                       f"Compare largest so far {arr[largest]} with right child {arr[right]}.")
                if arr[right] > arr[largest]:
                    largest = right

            if largest == root:
                return

            message = (f"Swap parent {arr[root]} with larger child "
                       f"{arr[largest]} to restore the heap.")
            arr[root], arr[largest] = arr[largest], arr[root]
            swaps += 1
            record("swap", [root, largest], size, message)
            root = largest

    record("start", [], n, "Initial array.")

    for i in range(n // 2 - 1, -1, -1):
        record("build", [], n, f"Build max-heap: heapify the subtree at index {i}.")
        heapify(n, i)

    for end in range(n - 1, 0, -1):
        message = f"Move the max {arr[0]} to index {end}. It is now in its final position."
        arr[0], arr[end] = arr[end], arr[0]
        swaps += 1
        record("extract", [0, end], end, message)
        heapify(end, 0)

    record("sorted", [], 0, "Array is sorted.")

    return {
        "steps": steps,
        "comparisons": comparisons,
        "swaps": swaps,
        "sorted_array": arr.copy(),
    }