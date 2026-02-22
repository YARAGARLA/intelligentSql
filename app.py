import streamlit as st
import sqlite3
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("Please add your GOOGLE_API_KEY in the .env file")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)

# ✅ FIXED MODEL NAME
model = genai.GenerativeModel("gemini-1.5-flash")
# Function to convert natural language to SQL
def get_sql_query(question):
    prompt = f"""
Convert the following natural language question into SQL query.

Database: Students
Columns: name, class, marks, company

Question: {question}

Only return SQL query without explanation.
"""
    response = model.generate_content(prompt)
    return response.text.strip()


# Function to execute SQL query
def run_sql_query(query):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        conn.close()
        return f"Error: {e}"


# Streamlit UI
st.title("IntelliSQL - Intelligent SQL Querying using Gemini Flash")

question = st.text_input("Enter your question:")

if st.button("Generate and Execute"):
    if question:
        sql_query = get_sql_query(question)

        st.subheader("Generated SQL Query:")
        st.code(sql_query, language="sql")

        result = run_sql_query(sql_query)

        st.subheader("Query Result:")
        st.write(result)
    else:
        st.warning("Please enter a question.")
