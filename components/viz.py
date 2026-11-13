import streamlit as st
import plotly.graph_objects as go

from components.ui import (
    apply_theme, hero, legend, explain, preset_buttons, learn_panel,
)


def sort_page(cfg):
    key = cfg["key"]

    st.set_page_config(page_title=f"{cfg['name']} | AlgoVision AI",
                       page_icon=cfg["icon"], layout="wide")
    apply_theme()
    hero(cfg["icon"], f"{cfg['name']} Visualizer", cfg["subtitle"])

    input_key = f"{key}_input"
    if input_key not in st.session_state:
        st.session_state[input_key] = cfg["default"]

    preset_buttons(input_key)
    user_input = st.text_input("Enter numbers separated by commas",
                               key=input_key)

    if st.button("Generate Visualization", type="primary",
                 key=f"{key}_generate"):
        try:
            arr = [int(x.strip()) for x in user_input.split(",") if x.strip()]
            if not arr:
                st.error("Enter at least one number.")
            elif len(arr) > 30:
                st.error("Maximum 30 numbers allowed.")
            else:
                st.session_state[f"{key}_result"] = cfg["fn"](arr)
                st.session_state[f"{key}_slider"] = 0
        except ValueError:
            st.error("Enter valid integers separated by commas.")

    data = st.session_state.get(f"{key}_result")
    if not data:
        st.info("Pick an example or enter numbers, then click "
                "**Generate Visualization**.")
    else:
        steps = data["steps"]

        step_number = st.slider("Navigate through sorting steps",
                                0, len(steps) - 1, key=f"{key}_slider")
        st.progress((step_number + 1) / len(steps))

        step = steps[step_number]
        values = step["array"]
        legend(cfg["legend"])

        fig = go.Figure(data=[go.Bar(
            x=list(range(len(values))), y=values,
            marker_color=cfg["colors"](step, len(values)),
            text=values, textposition="outside",
        )])
        fig.update_layout(title=f"{cfg['name']} Visualization",
                          xaxis_title="Array Index", yaxis_title="Value",
                          height=450, showlegend=False)
        st.plotly_chart(fig, use_container_width=True, key=f"{key}_chart")

        st.subheader(f"Step {step_number + 1} / {len(steps)}")
        explain(step["message"])
        st.write("Current Array:", values)

        st.divider()
        c1, c2, c3 = st.columns(3)
        c1.metric("Comparisons", data["comparisons"])
        c2.metric(cfg["moves_label"], data[cfg["moves_key"]])
        c3.metric("Array Size", len(values))

        if step["action"] == "sorted":
            st.success(f"Final Sorted Array: {data['sorted_array']}")
            st.balloons()

    st.divider()
    learn_panel(cfg["how"], cfg["pseudo"], cfg["complexity"], cfg["tips"])