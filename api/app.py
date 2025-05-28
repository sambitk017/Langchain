from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import uvicorn
import os
from typing import Any
from pydantic import BaseModel

class MyModel(BaseModel):
    data: Any  # Could cause issues if misused

load_dotenv()

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

llm_model = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5 years child with 100 words")

@app.post("/essay")
async def generate_essay(topic: str):
    response = llm_model(prompt1.format(topic=topic))
    return {"essay": response}

@app.post("/poem")
async def generate_poem(topic: str):
    response = llm_model(prompt2.format(topic=topic))
    return {"poem": response}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
