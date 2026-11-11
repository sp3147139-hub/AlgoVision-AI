
import streamlit as st

st.set_page_config(
    page_title="AlgoVision AI",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AlgoVision AI")

st.subheader(
    "Interactive Data Structures and Algorithms Visualizer"
)

st.write(
    "Learn DSA through interactive visualizations "
    "and AI-powered explanations."
)

st.divider()

st.header("Welcome!")

st.info(
    "Select Bubble Sort from the sidebar "
    "to start visualizing the algorithm."
)

st.markdown("""
### Current Features

- Bubble Sort Algorithm
- Step-by-Step Visualization
- Comparison Highlighting
- Swap Tracking
- Time Complexity Analysis

### Upcoming Features

- Selection Sort
- Insertion Sort
- Searching Algorithms
- AI Algorithm Explanations
""")
