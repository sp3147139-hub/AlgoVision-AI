
def selection_sort(arr):
    """
    Selection Sort with step-by-step visualization.
    Records comparisons, swaps and completed passes.
    """

    arr = arr.copy()
    n = len(arr)
    steps = []

    steps.append({
        "array": arr.copy(),
        "comparing": [],
        "minimum": None,
        "action": "start",
        "message": "Starting Selection Sort"
    })

    comparisons = 0
    swaps = 0

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            comparisons += 1

            steps.append({
                "array": arr.copy(),
                "comparing": [min_index, j],
                "minimum": min_index,
                "action": "compare",
                "message": (
                    f"Comparing {arr[min_index]} and {arr[j]}"
                )
            })

            if arr[j] < arr[min_index]:
                min_index = j

                steps.append({
                    "array": arr.copy(),
                    "comparing": [i, min_index],
                    "minimum": min_index,
                    "action": "minimum",
                    "message": (
                        f"New minimum found: {arr[min_index]}"
                    )
                })

        # Swap minimum with current position
        if min_index != i:

            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

            steps.append({
                "array": arr.copy(),
                "comparing": [i, min_index],
                "minimum": i,
                "action": "swap",
                "message": (
                    f"Swapped {arr[i]} and {arr[min_index]}"
                )
            })

        steps.append({
            "array": arr.copy(),
            "comparing": [],
            "minimum": i,
            "action": "pass",
            "message": f"Pass {i + 1} completed"
        })

    steps.append({
        "array": arr.copy(),
        "comparing": [],
        "minimum": None,
        "action": "sorted",
        "message": "Selection Sort completed!"
    })

    return {
        "steps": steps,
        "comparisons": comparisons,
        "swaps": swaps,
        "sorted_array": arr
    }
