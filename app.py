import streamlit as st
from utils import load_vectorstore, search_context
from compliance_checker import load_rules, check_compliance

st.set_page_config(page_title="Medical Compliance Checker", layout="wide")

st.title("🩺 Medical RAG – Policy Compliance Checker")

st.write("Upload PDFs → Build Vectorstore → Ask Query → Check Against 15 Rules.")

# Load rules
rules = load_rules()

# Load the vectorstore
st.sidebar.header("Vectorstore")
if st.sidebar.button("Load Vectorstore"):
    try:
        vectorstore = load_vectorstore()
        st.sidebar.success("Vectorstore loaded!")
    except:
        st.sidebar.error("Vectorstore missing. Run ingest.py first.")

query = st.text_input("Enter your medical question / text to evaluate:")

if st.button("Check Compliance"):
    if not query:
        st.error("Enter a query first.")
    else:
        st.subheader("🔎 Retrieving Relevant Context")
        context = search_context(vectorstore, query)
        st.write(context)

        st.subheader("🧠 Running Compliance Check...")
        results = check_compliance(context, rules)

        st.subheader("📋 Final Compliance Report")

        for r in results:
            st.write(f"### Rule {r['rule_id']} — {r['rule_title']}")
            st.write(r["result"])
            st.markdown("---")
