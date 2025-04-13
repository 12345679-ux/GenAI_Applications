import requests
import streamlit as st


def get_groq_response(input_text, target_language):
    json_body={
  "input": {
    "language": target_language,
    "text": input_text
  },
  "config": {},
  "kwargs": {}
}
    response=requests.post("http://127.0.0.1:8000/chain/invoke",json=json_body)

    response_data = response.json()

    Translated_Text = response_data.get("output","Translation Failed")


    return Translated_Text

## Streamlit app
st.title("Multi-Language Translator")

languages = {
    "French": "French",
    "Spanish": "Spanish", 
    "German": "German",
    "Italian": "Italian",
    "Hindi": "Hindi"
}


selected_lang = st.selectbox("Choose target language", list(languages.keys()))
input_text=st.text_input("Enter text to translate")

if input_text:
    translation = get_groq_response(input_text, languages[selected_lang])
    st.subheader("Translation:")
    st.write(translation)