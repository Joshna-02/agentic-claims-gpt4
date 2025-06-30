import streamlit as st
from extractor import extract_text_from_pdf
from agent import triage_with_agent
from triage_tool import rule_based_triage

st.set_page_config(page_title="Claims Triage Assistant", page_icon="🧠")

st.title("🧠 AI Claims Triage Assistant")
st.markdown("Upload a healthcare claim PDF and let the agent decide: **Approve, Review, or Escalate**.")

uploaded_file = st.file_uploader("📄 Upload Healthcare Claim PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("🔍 Extracting text..."):
        extracted_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📑 Extracted Text")
    st.write(extracted_text)

    if st.button("🤖 Run AI Triage"):
        with st.spinner("🧠 GPT-3.5 + Rules-based evaluation..."):
            gpt_decision = triage_with_agent(extracted_text)
            rule_decision = rule_based_triage(extracted_text)

        st.success(f"🤖 GPT-3.5 Decision: **{gpt_decision}**")
        st.info(f"📏 Rule-Based Decision: **{rule_decision}**")

        if gpt_decision != rule_decision:
            st.warning("⚠️ Decisions don't match – consider escalation or manual review.")
