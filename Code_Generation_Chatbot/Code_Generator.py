import streamlit as st
import pandas as pd
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the model
model = ChatGroq(model="Llama3-8b-8192", groq_api_key="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")

# Define the prompt template
prompt = ChatPromptTemplate(
    [
        ("system", "You are an AI assistant specialized in generating Python code for data cleaning and EDA based on user input."),
        ("user", "{user_input}")
    ]
)

# Function to generate response (code generation)
def generate_response(user_input, dataset_name, columns):
    llm = model
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    
    # Pass dataset name and columns to the model to generate the code
    response = chain.invoke({
        'user_input': f"Given a dataset named '{dataset_name}' with columns {columns}, " + user_input
    })
    
    # Return the response (code)
    return response

# Streamlit UI setup
st.title("AI-Powered Data Science Assistant")
st.write("Upload your dataset")

uploaded_file = st.file_uploader("Please upload your dataset.")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    dataset_name = uploaded_file.name
    columns = list(data.columns)
    
    # Display dataset overview
    st.write("Dataset Overview:")
    st.write(data.head())

    st.subheader("Ask the AI assistant")
    user_input = st.text_input("Please enter your question here. Example: Can you show the correlation heatmap?")

    if user_input:
        # Generate the code using the LLM based on the dataset name and column names
        response = generate_response(user_input, dataset_name, columns)
        st.write("Generated Python code:")
        st.code(response)
    
else:
    st.info("Please upload your dataset to start the conversation.")
