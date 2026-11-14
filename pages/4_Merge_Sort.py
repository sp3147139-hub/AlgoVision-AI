from algorithms.merge_sort import merge_sort
from components.viz import sort_page


def colors(step, n):
    if step["action"] == "sorted":
        return ["#2ECC71"] * n
    lo, hi = step["range"] if step["range"] else (-1, -1)
    out = []
    for i in range(n):
        if i in step["comparing"]:
            out.append("#FF4B4B")
        elif lo <= i <= hi:
            out.append("#F1C40F")
        else:
            out.append("#3498DB")
    return out


sort_page({
    "key": "merge",
    "name": "Merge Sort",
    "icon": "🔀",
    "subtitle": "Split the array in half, sort each half, then merge them back together.",
    "default": "38, 27, 43, 3, 9, 82, 10",
    "fn": merge_sort,
    "colors": colors,
    "moves_label": "Writes",
    "moves_key": "writes",
    "legend": [
        ("#F1C40F", "Section being split / merged"),
        ("#FF4B4B", "Slot being filled"),
        ("#3498DB", "Outside current section"),
        ("#2ECC71", "Sorted (final)"),
    ],
    "how": [
        "Split the array in half, again and again, until each piece has 1 element.",
        "A single element is already sorted.",
        "Merge two sorted halves by repeatedly taking the smaller front element.",
        "Keep merging upward until one sorted array remains.",
    ],
    "pseudo": (
        "merge_sort(lo, hi):\n"
        "    if lo >= hi: return\n"
        "    mid = (lo + hi) // 2\n"
        "    merge_sort(lo, mid)\n"
        "    merge_sort(mid+1, hi)\n"
        "    merge(lo, mid, hi)"
    ),
    "complexity": {"best": "O(n log n)", "average": "O(n log n)",
                   "worst": "O(n log n)", "space": "O(n)", "stable": "Yes"},
    "tips": [
        "Same O(n log n) on every input, so there is no bad case.",
        "Needs O(n) extra memory for the halves.",
        "Try a long reversed input and compare the comparison count with bubble sort.",
        "Stable: equal values keep their order.",
    ],
}) 