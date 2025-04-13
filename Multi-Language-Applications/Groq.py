from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv

load_dotenv()

grok_api_key = os.getenv("GROQ_API_KEY")
llm  = ChatGroq(model="deepseek-r1-distill-qwen-32b",groq_api_key = grok_api_key)  


system_template = "translate the following into {language}"

prompttemplate = ChatPromptTemplate.from_messages([
    ('system',system_template),
    ('user','{text}')
])

parser = StrOutputParser()

chain = prompttemplate|llm|parser



app = FastAPI(title="Langchain Server",version="1.0",description="A simple app using langchain runnable inference")

add_routes(app,chain,path="/chain")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1", port  = 8000)
