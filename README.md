# 🚀 AlgoVision-AI

An interactive **Data Structures & Algorithms visualizer** built with Streamlit and Plotly. Watch algorithms run step by step instead of just reading about them. 🧠✨

## ✨ Features

- 🎬 Step-by-step slider with color-coded bars for every algorithm
- 💬 Plain-language explanation for each step
- 📊 Live counters for comparisons and swaps/shifts/writes
- 🎲 Quick example inputs: random, reversed (worst case), already sorted (best case), duplicates
- 📖 Learn panel per algorithm: how it works, pseudocode, time/space complexity, tips
- ✅ Automated tests for every algorithm (pytest)

## 🧮 Algorithms Available

| Page | Algorithm | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|---|
| 📥 | Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| 🎯 | Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| 🫧 | Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| 🔀 | Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |

## 📁 Project Structure

```
AlgoVision-AI/
├── algorithms/          # 🧮 Algorithm logic, returns step-by-step records
│   ├── insertion_sort.py
│   ├── selection_sort.py
│   ├── bubble_sort.py
│   └── merge_sort.py
├── components/          # 🎨 Shared UI
│   ├── ui.py            #    Theme, hero banner, legend, learn panel
│   └── viz.py           #    Reusable sorting page (chart, slider, metrics)
├── pages/               # 📄 One Streamlit page per algorithm
│   ├── 1_Insertion_Sort.py
│   ├── 2_Selection_Sort.py
│   ├── 3_Bubble_Sort.py
│   ├── 4_Merge_Sort.py
│   └── tests/           # ✅ pytest tests, one file per algorithm
├── add.py               # ▶️ App entry point (home page)
├── conftest.py          # pytest configuration
├── requirements.txt     # 📦 Dependencies
└── README.md
```

## ⚡ Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/sp3147139-hub/AlgoVision-AI.git
cd AlgoVision-AI
```

### 2️⃣ Create a virtual environment (optional)

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app

```bash
streamlit run add.py
```

🌐 Then open **http://localhost:8501** in your browser.

## 🧪 Running Tests

```bash
python -m pytest pages/tests -v
```

## 🧩 How It Works

Each algorithm in `algorithms/` returns a dictionary:

```python
{
    "steps": [...],         # one record per step (action, array, highlights, message)
    "comparisons": 10,
    "swaps": 4,             # "shifts" for insertion sort, "writes" for merge sort
    "sorted_array": [...],
}
```

The page only reads this data and draws it, so the algorithm logic stays separate from the UI and is easy to test.

### ➕ Adding a new algorithm

1. Create `algorithms/<name>.py` that returns the dictionary above.
2. Create `pages/tests/test_<name>.py` with tests.
3. Create `pages/<n>_<Name>.py` that calls `sort_page({...})` from `components/viz.py` with colors, legend and learn-panel text.

## 🛠️ Tech Stack

- 🐍 Python
- 🎈 Streamlit
- 📈 Plotly
- ✅ pytest

## 🗺️ Roadmap

- [x] 📥 Insertion Sort
- [x] 🎯 Selection Sort
- [x] 🫧 Bubble Sort
- [x] 🔀 Merge Sort
- [ ] ⚡ Quick Sort
- [ ] 🔍 Searching (linear and binary)
- [ ] 🧱 Linked list, stack, queue
- [ ] 🌳 Trees and graphs
- [ ] 🤖 AI-powered explanations of each step
- [ ] ☁️ Deploy on Streamlit Community Cloud

## 🤝 Contributing

Contributions are welcome! 🙌 Fork the repo, create a branch, and open a pull request. Please add tests for any new algorithm.

## 👨‍💻 Author

**Suhas Patil** — [@sp3147139-hub](https://github.com/sp3147139-hub)

⭐ If you like this project, give it a star!
