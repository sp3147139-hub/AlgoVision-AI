
def bubble_sort(arr):
    """
    Bubble Sort with step-by-step tracking.
    Returns the sorting steps for visualization.
    """

    arr = arr.copy()
    n = len(arr)
    steps = []

    steps.append({
        "array": arr.copy(),
        "comparing": [],
        "action": "start",
        "message": "Starting Bubble Sort"
    })

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):

            steps.append({
                "array": arr.copy(),
                "comparing": [j, j + 1],
                "action": "compare",
                "message": f"Comparing {arr[j]} and {arr[j + 1]}"
            })

            if arr[j] > arr[j + 1]:
                left, right = arr[j], arr[j + 1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

                steps.append({
                    "array": arr.copy(),
                    "comparing": [j, j + 1],
                    "action": "swap",
                    "message": f"Swapped {left} and {right}"
                })

        steps.append({
            "array": arr.copy(),
            "comparing": [],
            "action": "pass",
            "message": f"Pass {i + 1} completed"
        })

        if not swapped:
            break

    steps.append({
        "array": arr.copy(),
        "comparing": [],
        "action": "sorted",
        "message": "Array sorted successfully!"
    })

    return steps
