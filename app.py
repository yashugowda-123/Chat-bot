import streamlit as st
import openai
import PyPDF2
import io

# Set your OpenAI API key
openai.api_key = st.secrets["QqNjj2btQCoX2Or1pK0s9Pr7QE9f5S1c7RXCLmfPhJx8KjDnEA49CK29q55373XsLUsT6FOdyfT3BlbkFJJZf_Yy6K2r1RQi2CZLwVjPO1VAPFIjiiieqjS9KrNvivKCnPqSgzD-W8_6HvlKB5oamEH-CDUA"]  # or use st.text_input + st.session_state

st.title("📄 Ask AI Anything About Your PDF")

# Upload PDF
pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    st.text_area("Extracted Text", text[:2000], height=200)  # show preview

    question = st.text_input("Ask a question about the PDF")
    if st.button("Ask"):
        if question.strip():
            with st.spinner("Thinking..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": f"Here's a document: {text[:3000]} \n\nAnswer this: {question}"},
                    ],
                    temperature=0.2,
                )
                st.success(response.choices[0].message["content"])
