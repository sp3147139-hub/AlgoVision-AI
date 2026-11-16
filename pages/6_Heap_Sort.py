from algorithms.heap_sort import heap_sort
from components.viz import sort_page


def colors(step, n):
    out = []
    for i in range(n):
        if step["action"] == "sorted" or i >= step["heap_size"]:
            out.append("#2ECC71")
        elif i in step["comparing"]:
            out.append("#FF4B4B")
        else:
            out.append("#3498DB")
    return out


sort_page({
    "key": "heap",
    "name": "Heap Sort",
    "icon": "🌳",
    "subtitle": "Build a max-heap, then repeatedly move the largest value to the end.",
    "default": "12, 11, 13, 5, 6, 7",
    "fn": heap_sort,
    "colors": colors,
    "moves_label": "Swaps",
    "moves_key": "swaps",
    "legend": [
        ("#FF4B4B", "Comparing / swapping"),
        ("#3498DB", "Inside the heap"),
        ("#2ECC71", "Sorted (final)"),
    ],
    "how": [
        "Treat the array as a binary tree: the children of index i are at 2i+1 and 2i+2.",
        "Build a max-heap so every parent is at least as large as its children.",
        "Swap the root (the maximum) with the last heap element. It is now final.",
        "Shrink the heap by one, restore the heap property, and repeat.",
    ],
    "pseudo": (
        "build max-heap\n"
        "for end in n-1 .. 1:\n"
        "    swap a[0], a[end]\n"
        "    heapify(a, size=end, root=0)\n"
        "\n"
        "heapify(size, root):\n"
        "    largest = root\n"
        "    if left < size and a[left] > a[largest]: largest = left\n"
        "    if right < size and a[right] > a[largest]: largest = right\n"
        "    if largest != root: swap; heapify(size, largest)"
    ),
    "complexity": {"best": "O(n log n)", "average": "O(n log n)",
                   "worst": "O(n log n)", "space": "O(1)", "stable": "No"},
    "tips": [
        "Guaranteed O(n log n) like merge sort, but sorts in place with O(1) extra memory.",
        "Usually slower than quick sort in practice because of scattered memory access.",
        "Not stable: equal values can change order.",
        "Try 'Already sorted' and 'Reversed': the work stays about the same.",
    ],
})