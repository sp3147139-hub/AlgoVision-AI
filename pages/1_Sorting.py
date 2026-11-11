
import streamlit as st
import plotly.graph_objects as go

from algorithms.sorting import bubble_sort

st.set_page_config(
    page_title="Bubble Sort | AlgoVision AI",
    page_icon="🔄",
    layout="wide"
)

st.title("🔄 Bubble Sort Visualizer")
st.write("Watch how Bubble Sort arranges numbers step by step.")

st.divider()

# Input section
user_input = st.text_input(
    "Enter numbers separated by commas",
    value="5, 3, 8, 1, 2"
)

if st.button("Generate Visualization", type="primary"):

    try:
        numbers = [
            int(x.strip())
            for x in user_input.split(",")
            if x.strip()
        ]

        if not numbers:
            st.error("Please enter at least one number.")

        elif len(numbers) > 30:
            st.error("Maximum 30 numbers allowed.")

        else:
            st.session_state.steps = bubble_sort(numbers)
            st.session_state.original = numbers
            st.session_state.show_visualization = True

    except ValueError:
        st.error("Enter valid integers separated by commas.")

# Visualization section
if st.session_state.get("show_visualization", False):

    steps = st.session_state.steps

    st.subheader("Sorting Animation")

    step_number = st.slider(
        "Navigate through sorting steps",
        min_value=0,
        max_value=len(steps) - 1,
        value=0
    )

    current_step = steps[step_number]

    values = current_step["array"]
    comparing = current_step["comparing"]

    # Highlight compared elements
    colors = [
        "red" if i in comparing else "royalblue"
        for i in range(len(values))
    ]

    # Create chart
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
        title="Bubble Sort Visualization",
        xaxis_title="Array Index",
        yaxis_title="Value",
        height=450,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    # Display step information
    st.subheader(
        f"Step {step_number + 1} of {len(steps)}"
    )

    st.info(current_step["message"])

    st.write("Current Array:", values)

    if current_step["action"] == "compare":
        st.warning("Comparing adjacent elements.")

    elif current_step["action"] == "swap":
        st.success("Elements swapped!")

    elif current_step["action"] == "sorted":
        st.success("Sorting completed!")

    # Complexity
    st.divider()
    st.subheader("Algorithm Complexity")

    col1, col2, col3 = st.columns(3)

    col1.metric("Best Case", "O(n)")
    col2.metric("Average Case", "O(n²)")
    col3.metric("Worst Case", "O(n²)")

    st.write("Auxiliary Space Complexity: O(1)")
