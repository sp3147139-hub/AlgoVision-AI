from algorithms.insertion_sort import insertion_sort
from components.viz import sort_page


def colors(step, n):
    out = []
    for i in range(n):
        if step["action"] == "sorted":
            out.append("#2ECC71")
        elif i == step["key_index"]:
            out.append("#F1C40F")
        elif i in step["comparing"]:
            out.append("#FF4B4B")
        elif i <= step["sorted_upto"]:
            out.append("#2ECC71")
        else:
            out.append("#3498DB")
    return out


sort_page({
    "key": "insertion",
    "name": "Insertion Sort",
    "icon": "📥",
    "subtitle": "Watch it build a sorted section by inserting one element at a time.",
    "default": "12, 11, 13, 5, 6",
    "fn": insertion_sort,
    "colors": colors,
    "moves_label": "Shifts",
    "moves_key": "shifts",
    "legend": [
        ("#F1C40F", "Key being inserted"),
        ("#FF4B4B", "Compared / shifted"),
        ("#2ECC71", "Sorted section"),
        ("#3498DB", "Unsorted"),
    ],
    "how": [
        "The first element is a sorted section of size 1.",
        "Pick the next element as the key.",
        "Compare the key with the sorted section right to left, shifting larger values one step right.",
        "Drop the key into the gap. The sorted section grows by one. Repeat.",
    ],
    "pseudo": (
        "for i in 1 .. n-1:\n"
        "    key = a[i]\n"
        "    j = i - 1\n"
        "    while j >= 0 and a[j] > key:\n"
        "        a[j+1] = a[j]\n"
        "        j = j - 1\n"
        "    a[j+1] = key"
    ),
    "complexity": {"best": "O(n)", "average": "O(n²)", "worst": "O(n²)",
                   "space": "O(1)", "stable": "Yes"},
    "tips": [
        "Best case is sorted input: n-1 comparisons, 0 shifts.",
        "Worst case is reversed input.",
        "Fast on small or nearly sorted data.",
        "Stable: equal values keep their order.",
    ],
})