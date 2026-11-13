from algorithms.selection_sort import selection_sort
from components.viz import sort_page


def colors(step, n):
    out = []
    for i in range(n):
        if step["action"] == "sorted":
            out.append("#2ECC71")
        elif i in step["comparing"]:
            out.append("#FF4B4B")
        elif i == step["minimum"]:
            out.append("#F1C40F")
        else:
            out.append("#3498DB")
    return out


sort_page({
    "key": "selection",
    "name": "Selection Sort",
    "icon": "🎯",
    "subtitle": "Watch it find the smallest element and lock it into place.",
    "default": "64, 25, 12, 22, 11",
    "fn": selection_sort,
    "colors": colors,
    "moves_label": "Swaps",
    "moves_key": "swaps",
    "legend": [
        ("#FF4B4B", "Comparing / swapping"),
        ("#F1C40F", "Current minimum"),
        ("#3498DB", "Unsorted"),
        ("#2ECC71", "Sorted (final)"),
    ],
    "how": [
        "Treat the first unsorted position as the current minimum.",
        "Scan the rest; update the minimum whenever a smaller value appears.",
        "Swap the minimum into the first unsorted position.",
        "That position is final. Repeat for the remaining part.",
    ],
    "pseudo": (
        "for i in 0 .. n-2:\n"
        "    min = i\n"
        "    for j in i+1 .. n-1:\n"
        "        if a[j] < a[min]: min = j\n"
        "    if min != i: swap a[i], a[min]"
    ),
    "complexity": {"best": "O(n²)", "average": "O(n²)", "worst": "O(n²)",
                   "space": "O(1)", "stable": "No"},
    "tips": [
        "Always n(n-1)/2 comparisons, even on sorted input.",
        "At most n-1 swaps: good when writes are expensive.",
        "Not stable: equal values can change order.",
    ],
})