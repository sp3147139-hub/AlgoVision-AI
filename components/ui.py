import random

import streamlit as st

CSS = """
<style>
.hero {
    padding: 1.6rem 2rem; border-radius: 16px; margin-bottom: 1rem;
    background: linear-gradient(135deg, #1f3c88 0%, #6a11cb 100%);
    color: white;
}
.hero h1 { margin: 0; font-size: 2.2rem; color: white; }
.hero p  { margin: .4rem 0 0; opacity: .9; font-size: 1.05rem; }
.legend { display: flex; gap: .6rem; flex-wrap: wrap; margin: .5rem 0 1rem; }
.chip {
    display: inline-flex; align-items: center; gap: .45rem;
    padding: .25rem .8rem; border-radius: 999px; font-size: .85rem;
    background: rgba(128,128,128,.15);
}
.dot { width: 12px; height: 12px; border-radius: 50%; display: inline-block; }
.explain {
    padding: .9rem 1.1rem; border-radius: 12px; margin: .5rem 0;
    border-left: 5px solid #6a11cb; background: rgba(106,17,203,.10);
    font-size: 1.05rem;
}
[data-testid="stMetric"] {
    background: rgba(128,128,128,.12); padding: .8rem 1rem; border-radius: 12px;
}
</style>
"""


def apply_theme():
    st.markdown(CSS, unsafe_allow_html=True)


def hero(icon, title, subtitle):
    st.markdown(
        f'<div class="hero"><h1>{icon} {title}</h1><p>{subtitle}</p></div>',
        unsafe_allow_html=True,
    )


def legend(items):
    """items: list of (hex_color, label)."""
    chips = "".join(
        f'<span class="chip"><span class="dot" style="background:{c}"></span>{l}</span>'
        for c, l in items
    )
    st.markdown(f'<div class="legend">{chips}</div>', unsafe_allow_html=True)


def explain(message):
    st.markdown(f'<div class="explain">💡 {message}</div>', unsafe_allow_html=True)


def preset_buttons(input_key):
    """One-click sample inputs. input_key must be the text_input's key."""
    presets = {
        "🎲 Random": lambda: ", ".join(str(random.randint(-20, 99)) for _ in range(8)),
        "📉 Reversed (worst)": lambda: "9, 8, 7, 6, 5, 4, 3, 2, 1",
        "✅ Already sorted (best)": lambda: "1, 2, 3, 4, 5, 6, 7, 8, 9",
        "🔁 Duplicates": lambda: "5, 3, 5, 1, 3, 1, 4",
    }

    def setter(make):
        st.session_state[input_key] = make()

    st.caption("Quick examples:")
    for col, (label, make) in zip(st.columns(len(presets)), presets.items()):
        col.button(label, on_click=setter, args=(make,),
                   use_container_width=True, key=f"{input_key}_{label}")


def learn_panel(how_it_works, pseudocode, complexity, tips):
    """
    how_it_works: list[str]
    pseudocode:   str
    complexity:   dict with best, average, worst, space, stable
    tips:         list[str]
    """
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📖 How it works", "🧾 Pseudocode", "⏱ Complexity", "🧠 Tips"]
    )
    with tab1:
        for i, text in enumerate(how_it_works, 1):
            st.markdown(f"**{i}.** {text}")
    with tab2:
        st.code(pseudocode, language="text")
    with tab3:
        cols = st.columns(5)
        for col, (label, key) in zip(
            cols,
            [("Best", "best"), ("Average", "average"), ("Worst", "worst"),
             ("Space", "space"), ("Stable", "stable")],
        ):
            col.metric(label, complexity[key])
    with tab4:
        for tip in tips:
            st.markdown(f"- {tip}")