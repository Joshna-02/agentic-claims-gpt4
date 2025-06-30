# 🧠 Agentic Claims Triage Assistant (GPT-3.5 + LangChain)

An autonomous AI agent that reads healthcare claim PDFs and determines whether to approve, review, or escalate them using GPT-3.5 and LangChain.

---

## ⚙️ Tech Stack

- **LLM**: OpenAI GPT-3.5 Turbo
- **Agent Framework**: LangChain
- **PDF Extraction**: pdfplumber
- **UI**: Streamlit
- **Custom Logic**: Python tools (triage rules)
- **Deployment**: Local or Streamlit Cloud

---

## 📁 Project Structure
agentic-claims-gpt4/
│
├── app.py               # Main Streamlit app
├── agent.py             # GPT-3.5 LangChain agent logic
├── extractor.py         # Extracts text from PDFs
├── triage_tool.py       # Optional rules-based classifier
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/Joshna-02/agentic-claims-gpt4.git
cd agentic-claims-gpt4
pip install -r requirements.txt
echo OPENAI_API_KEY=your_key_here > .env
streamlit run app.py

1. Summarize patient and diagnosis info
2. Detect missing fields or red flags
3. Classify: [Urgent] [Needs Review] [Approve]
4. Justify decision with 2–3 bullet points
