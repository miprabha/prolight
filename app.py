import streamlit as st
from backend import get_values

st.set_page_config(page_title="prolight", layout="wide")
st.title("🧬 ProLIGHT: Highlight Genes, Proteins, and Diseases")

user_input = st.text_area("Paste a biomedical abstract:", height=300)

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        entities = get_values(user_input)
        highlighted = user_input

        # Insert highlighting in reverse to preserve indices
        for ent in sorted(entities, key=lambda x: -x["start"]):
            tag = f"<span style='background-color:#ffff99;' title='{ent['label']}'><b>{ent['text']}</b></span>"
            highlighted = highlighted[:ent["start"]] + tag + highlighted[ent["end"]:]

        st.markdown("### 🔍 Highlighted Output:")
        st.markdown(f"<div style='line-height:1.8;'>{highlighted}</div>", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 📋 Extracted Entities Table:")
        st.table(entities)