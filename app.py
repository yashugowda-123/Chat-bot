import streamlit as st
import openai
from google.cloud import translate_v2 as translate
import os

# 🔐 Define API keys directly in this file
OPENAI_API_KEY = "QqNjj2btQCoX2Or1pK0s9Pr7QE9f5S1c7RXCLmfPhJx8KjDnEA49CK29q55373XsLUsT6FOdyfT3BlbkFJJZf_Yy6K2r1RQi2CZLwVjPO1VAPFIjiiieqjS9KrNvivKCnPqSgzD-W8_6HvlKB5oamEH-CDUA"
GOOGLE_API_KEY = "AIzaSyAX7TGpaaiszs1Z3Rn1Dp4vXpFOPnk0MfU"  # Only needed if you're using unofficial API or setting env manually

# ✅ Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Optional: Set Google Application Credentials if using official Google Cloud API
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_google_credentials.json"

st.set_page_config(page_title="PYQ AI Assistant", page_icon="📘")

st.title("📘 PYQ Similar Question Generator")

user_question = st.text_input("Enter your PYQ question:")

if user_question:
    with st.spinner("Generating similar question..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Generate a similar question for: {user_question}"}
            ]
        )
        sim_q = response['choices'][0]['message']['content']
        st.success("✅ Similar Question:")
        st.markdown(sim_q)

    # 🌐 Translate to Hindi using Google Translate API
    try:
        client = translate.Client()
        translated = client.translate(sim_q, target_language='hi')
        st.info(f"🌐 Hindi Translation: {translated['translatedText']}")
    except Exception as e:
        st.error("Translation failed. Make sure your Google credentials are set up.")