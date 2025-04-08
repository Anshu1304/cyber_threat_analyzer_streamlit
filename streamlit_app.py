import streamlit as st
from gpt_helper2 import GPTHelper

st.set_page_config(page_title="Cyber Threat Analyzer", layout="wide")
st.title("🛡️ Cyber Threat Analyzer")
st.markdown("Analyze and tag cyber threats using AI (Gemma model via OpenRouter)")

# Initialize GPT Helper
gpt = GPTHelper()

# Create sidebar menu
option = st.sidebar.radio("Select an action:", ["🔍 Analyze Threat", "🏷️ Tag Threat Data"])

# Threat Analyzer UI
if option == "🔍 Analyze Threat":
    st.header("🔍 Threat Analysis")
    query = st.text_area("Enter threat description to analyze:")
    if st.button("Analyze"):
        with st.spinner("Analyzing threat data using AI..."):
            result = gpt.analyze_threat(query)
            st.subheader("📌 AI Response")
            if result.get("status") == "success":
                st.write(result["data"].get("content", "No detailed response returned."))
            else:
                st.error(result.get("error", "Unknown error occurred."))

# Threat Tagger UI
elif option == "🏷️ Tag Threat Data":
    st.header("🏷️ Threat Tagger")
    data = st.text_area("Enter raw threat data to tag:")
    if st.button("Tag"):
        with st.spinner("Tagging data using AI..."):
            result = gpt.tag_threat_data(data)
            st.subheader("📌 Tagged Result")
            if result.get("status") == "success":
                st.json(result["data"])
            else:
                st.error(result.get("error", "Tagging failed."))