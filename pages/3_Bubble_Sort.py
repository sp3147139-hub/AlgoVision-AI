from algorithms.bubble_sort import bubble_sort
from components.viz import sort_page


def colors(step, n):
    out = []
    for i in range(n):
        if step["action"] == "sorted" or i >= step["sorted_from"]:
            out.append("#2ECC71")
        elif i in step["comparing"]:
            out.append("#FF4B4B")
        else:
            out.append("#3498DB")
    return out


sort_page({
    "key": "bubble",
    "name": "Bubble Sort",
    "icon": "🫧",
    "subtitle": "Watch the largest values bubble to the end, pass by pass.",
    "default": "64, 34, 25, 12, 22, 11, 90",
    "fn": bubble_sort,
    "colors": colors,
    "moves_label": "Swaps",
    "moves_key": "swaps",
    "legend": [
        ("#FF4B4B", "Comparing / swapping"),
        ("#2ECC71", "Sorted (final)"),
        ("#3498DB", "Unsorted"),
    ],
    "how": [
        "Compare each pair of neighbors from left to right.",
        "Swap them if the left one is larger.",
        "After each pass, the largest remaining value has bubbled to the end.",
        "Stop early if a pass makes no swaps.",
    ],
    "pseudo": (
        "for i in 0 .. n-2:\n"
        "    swapped = false\n"
        "    for j in 0 .. n-2-i:\n"
        "        if a[j] > a[j+1]: swap; swapped = true\n"
        "    if not swapped: break"
    ),
    "complexity": {"best": "O(n)", "average": "O(n²)", "worst": "O(n²)",
                   "space": "O(1)", "stable": "Yes"},
    "tips": [
        "Best case is sorted input thanks to the early exit.",
        "Usually the most swaps of the three, so it's rarely used in practice.",
        "Stable: equal values keep their order.",
    ],
})