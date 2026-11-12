
import streamlit as st
import plotly.graph_objects as go

from algorithms.selection_sort import selection_sort

st.set_page_config(
    page_title="Selection Sort | AlgoVision AI",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Selection Sort Visualizer")

st.write(
    "Watch how Selection Sort finds the smallest "
    "element and places it in the correct position."
)

st.divider()

# Input
user_input = st.text_input(
    "Enter numbers separated by commas",
    "64, 25, 12, 22, 11"
)

if st.button("Generate Visualization", type="primary"):

    try:
        arr = [
            int(x.strip())
            for x in user_input.split(",")
            if x.strip()
        ]

        if not arr:
            st.error("Enter at least one number.")

        elif len(arr) > 30:
            st.error("Maximum 30 numbers allowed.")

        else:
            result = selection_sort(arr)

            st.session_state.selection_steps = result["steps"]
            st.session_state.selection_comparisons = result["comparisons"]
            st.session_state.selection_swaps = result["swaps"]
            st.session_state.selection_result = result["sorted_array"]
            st.session_state.selection_ready = True

    except ValueError:
        st.error("Enter valid integers separated by commas.")

# Visualization
if st.session_state.get("selection_ready", False):

    steps = st.session_state.selection_steps

    step_number = st.slider(
        "Navigate through sorting steps",
        0,
        len(steps) - 1,
        key="selection_slider"
    )

    step = steps[step_number]
    values = step["array"]
    comparing = step["comparing"]
    minimum = step["minimum"]

    # Color the bars
    colors = []

    for i in range(len(values)):

        if i in comparing:
            colors.append("#FF4B4B")

        elif i == minimum:
            colors.append("#F1C40F")

        else:
            colors.append("#3498DB")

    # Plot
    fig = go.Figure(
        data=[
            go.Bar(
                x=list(range(len(values))),
                y=values,
                marker_color=colors,
                text=values,
                textposition="outside"
            )
        ]
    )

    fig.update_layout(
        title="Selection Sort Visualization",
        xaxis_title="Array Index",
        yaxis_title="Value",
        height=450,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    # Information
    st.subheader(f"Step {step_number + 1} / {len(steps)}")

    st.info(step["message"])

    st.write("Current Array:", values)

    st.divider()

    # Statistics
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Comparisons",
        st.session_state.selection_comparisons
    )

    col2.metric(
        "Swaps",
        st.session_state.selection_swaps
    )

    col3.metric(
        "Array Size",
        len(values)
    )

    if step["action"] == "sorted":
        st.success(
            f"Final Sorted Array: {st.session_state.selection_result}"
        )
        st.balloons()
