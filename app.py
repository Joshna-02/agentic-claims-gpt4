import streamlit as st
from extractor import extract_text_from_pdf
from agent import run_langchain_agent
from triage_tool import rule_based_triage

st.set_page_config(page_title="Agentic Claims Triage Assistant", layout="wide")

st.title("🧠 Agentic AI Claims Triage Assistant")
st.markdown("Upload a healthcare claim PDF and get a triage recommendation using GPT-3.5 and LangChain.")

uploaded_file = st.file_uploader("Upload a claim PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from PDF..."):
        text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Extracted Text")
    st.code(text[:2000])  # Show first 2000 chars for preview

    with st.spinner("Running LangChain Agent..."):
        agent_decision = run_langchain_agent(text)

    rule_decision = rule_based_triage(text)

    st.subheader("🤖 GPT Agent Decision")
    st.success(agent_decision)

    st.subheader("🛠️ Rule-Based Recommendation")
    st.info(rule_decision)
