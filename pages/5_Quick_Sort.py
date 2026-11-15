from algorithms.quick_sort import quick_sort
from components.viz import sort_page


def colors(step, n):
    if step["action"] == "sorted":
        return ["#2ECC71"] * n
    lo, hi = step["range"] if step["range"] else (-1, -1)
    out = []
    for i in range(n):
        if i == step["pivot"]:
            out.append("#9B59B6")
        elif i in step["comparing"]:
            out.append("#FF4B4B")
        elif i in step["fixed"]:
            out.append("#2ECC71")
        elif lo <= i <= hi:
            out.append("#3498DB")
        else:
            out.append("#7F8C8D")
    return out


sort_page({
    "key": "quick",
    "name": "Quick Sort",
    "icon": "⚡",
    "subtitle": "Pick a pivot, move smaller values left and larger values right, then repeat.",
    "default": "10, 80, 30, 90, 40, 50, 70",
    "fn": quick_sort,
    "colors": colors,
    "moves_label": "Swaps",
    "moves_key": "swaps",
    "legend": [
        ("#9B59B6", "Pivot"),
        ("#FF4B4B", "Comparing / swapping"),
        ("#3498DB", "Current partition"),
        ("#7F8C8D", "Waiting (other partitions)"),
        ("#2ECC71", "Final position"),
    ],
    "how": [
        "Pick a pivot (this page uses the last element of the section).",
        "Scan the section; move every value smaller than the pivot to the left side.",
        "Put the pivot between the small and large values. It is now in its final spot.",
        "Repeat on the left part and the right part separately.",
    ],
    "pseudo": (
        "quick_sort(lo, hi):\n"
        "    if lo >= hi: return\n"
        "    pivot = a[hi]; i = lo - 1\n"
        "    for j in lo .. hi-1:\n"
        "        if a[j] < pivot: i += 1; swap a[i], a[j]\n"
        "    swap a[i+1], a[hi]\n"
        "    quick_sort(lo, i)\n"
        "    quick_sort(i+2, hi)"
    ),
    "complexity": {"best": "O(n log n)", "average": "O(n log n)",
                   "worst": "O(n²)", "space": "O(log n)", "stable": "No"},
    "tips": [
        "Usually the fastest of these in practice, with few extra writes.",
        "Worst case happens with a bad pivot. Try 'Already sorted' or 'Reversed' to see it.",
        "Random pivots or median-of-three make the worst case unlikely.",
        "Not stable: equal values can change order.",
    ],
})